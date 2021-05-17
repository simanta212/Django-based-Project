from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	address = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__ (self):
		return self.user.username
		
Anime_Category=(
    ('C','Comedy'),
    ('A','Adventure'),
    ('D','Horror'),
    ('R','Romance'),
)
status_choices=(
    ('TR','Trending'),
    ('MV','Most Viewed'),
    ('RA','Recently Added'),
)

class Anime(models.Model):
	Anime_title = models.CharField(max_length=100)
	Anime_description = models.TextField()
	Anime_file = models.FileField(upload_to='Anime/')
	Anime_Category = models.CharField(choices=Anime_Category , max_length=1)
	Anime_view = models.IntegerField(default=0)
	Upload_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.Anime_title
	
	def delete(self, *args, **kwargs):
		self.Anime_file.delete()
		super().delete(*args, **kwargs)  

class Rating(models.Model):
	anime = models.ForeignKey(Anime,on_delete=models.CASCADE)
	rating = models.IntegerField() 
	date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.rating

class comment(models.Model):
	 message = models.TextField()
	 Created_date = models.DateTimeField(default=timezone.now)
	#prediction = models.CharField(max_length=20, default="NO Prediction")

    


	 