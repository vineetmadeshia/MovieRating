from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MoviesList(models.Model):
    movie_name=models.CharField(max_length=200,unique=True)
    movie_rating=models.FloatField()
    rating_users=models.CharField(max_length=200)


class WatchList(models.Model):
    movie_name=models.CharField(max_length=200)
    movie=models.ForeignKey(MoviesList,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

'''class Watched(models.Model):
    movie_name=models.CharField(max_length=200)
    movie=models.ForeignKey(MoviesList,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)'''
