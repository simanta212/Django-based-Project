from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate,login,logout
from .models import Anime,comment
 
from django.contrib import messages
import json 
from django.db.models import Q
from .reccopy import genre_recommendations

# Create your views here.
def user_login(request):# TO give access user
    if request.method == 'POST': # POST is used to insert/update remote data
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('members')
            # return redirect('login')
        else:
            return HttpResponse("Wrong Credientials")
    else: 
        if request.user.is_authenticated:
            return redirect('members')
        else: 
            return render(request, "login/login.html", context={})
    

def user_register(request):# To create new user
    if request.method == 'POST':
        first_name = request.POST['first_name']# Both name same as the name of field in html file
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        age = request.POST['age']
        address = request.POST['address']

        if password1==password2: #applying if/else conditions in registry form
            if User.objects.filter(username=username).exists():
                print("username taken")
            elif User.objects.filter(email=email).exists():
                print("email taken")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                UserProfile.objects.create(id=user.id,user = user,age=age,address=address)
                print('user created')
                return redirect('login')

    return render(request, "login/register.html", context={}) #requesting to redirect requested page

def user_logout(request): 
    logout(request)       
    return redirect('login')

def animelist(request):# To show lists of animes
    anime = Anime.objects.all()
    return render(request, "animelist.html", {'animes': anime})

def delete_anime(request,Anime_id):
    if request.method == "POST":
        anime = Anime.objects.get(pk=Anime_id)
        anime.delete() # To delete recorded data in the webapp
        return redirect('members')
    else:
        return redirect('anime')

def edit_anime(request,Anime_id):
    if request.method =="POST":
        anime = Anime.objects.get(pk=Anime_id)
        title = request.POST.get('animetitle')
        anime.Anime_title = title
        anime.save()        
        messages.success(request,("Editing done !!!"))
        return redirect('members')
    else:
        anime_obj = Anime.objects.get(pk=Anime_id)
        return render(request, 'edit.html',{'anime_obj': anime_obj})

def get_data_querys(query=None):
    queryset = []

    queries = query.split(" ") 
    for q in queries:
        animies = Anime.objects.filter(
            Q(Anime_title__icontains = q)
            ).distinct()

        for anime in animies:
            queryset.append(anime) 
        return list(set(queryset))

def search(request):  
    animes = ''
    if request.GET:
        query = request.GET['s']
        animes = get_data_querys(str(query))
        try:
            rec = genre_recommendations(query.lower())
        except:
            rec = ["recommendation not found"]
    return render(request, "search.html", {'animes': animes, "suggestion":rec})
    

#@login           #using decorator
def library(request):
    return render(request, "library.html", context={})

def comentu(request):
    comment_all = comment.objects.all()

    return render(request, "library.html", {'comments':comment_all})

def add_comment(request):
    if request.method == 'POST':
        comment_user = request.POST.get('comments')
        comment.objects.create(message=comment_user)

        return redirect('commentu')
    else:
        return render(request, "library.html", {'error':"error comment is invalid or method type is incorrect"})        
        

#def add_comment_to_post(request):


    #if request.method == 'POST':
        #form = CommentForm(request.POST)
        #if form.is_valid():
            #comment = form.save(commit=False)
            #comment.author = request.user
            #comment.post = post

           # unprocessed_feature = str(comment)
            # out = result(...)
            #print(unprocessed_feature)
