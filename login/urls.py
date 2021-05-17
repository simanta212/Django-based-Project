from django.urls import path
from . import views
#app_name = "login"
urlpatterns = [
    path('',views.animelist, name='anime'),
    path('delete/<Anime_id>',views.delete_anime, name='delete_anime'),
    path('edit/<Anime_id>',views.edit_anime, name='edit_anime'),
    path('login/',views.user_login, name='login'),
    path('register/',views.user_register, name='register'),
    path('logout/',views.user_logout,name="logout"),
    path('search/',views.search,name="search"),
    path('lib/',views.library,name="library"),
    path('comentu/',views.comentu,name="commentu"),
    path('addcomment/',views.add_comment,name="addcomment"),
    
]