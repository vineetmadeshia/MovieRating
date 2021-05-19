from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import MoviesList,WatchList


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MoviesList
        fields = ['url', 'movie_name', 'movie_rating', 'rating_users']

class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    movie=serializers.ReadOnlyField(source='movie.id')
    
    class Meta:
        model=WatchList
        fields = ['url', 'movie_name', 'movie', 'user']

    
    


'''class UserSerializer(serializers.ModelSerializer):
    watchlist = serializers.PrimaryKeyRelatedField(many=True, queryset=WatchList.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'watchlist']'''
