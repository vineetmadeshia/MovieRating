from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
#from .imdb_scrape import imdb
from .models import MoviesList,WatchList
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout

def registerPage(request):
    '''if request.user.is_authenticated:
        return redirect('home')
    else:'''
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username') 
            messages.success(request,'Account Created Succesfully for' +user)
            return redirect('login')

    context={'form':form}
    return render(request,'Movies/register.html',context)
    
        

def loginPage(request):
    '''if request.user.is_authenticated:
        return redirect('home')
    else:'''
    if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or password is incorrect')

    context={}
    return render(request,'Movies/login.html',context)

        

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    # imdb()
    cur_user=request.user
    detail=cur_user.watchlist_set.all()
    movies = MoviesList.objects.all()
    paginator = Paginator(movies, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'movies':movies,'detail':detail,'cur_user':cur_user,'page_obj':page_obj}
    return render(request,'Movies/Movielist.html',context)
 
        
 
        

def Moviedetail(request,pk):
    detail = MoviesList.objects.get(pk=pk)
    context={'detail':detail,}
    return render(request,'Movies/Moviedetails.html',context)
 #   imdb()
 
 
        

def Watchlist(request,pk):
    cur_user=request.user
    wlist=cur_user.watchlist_set.all()
    movies = MoviesList.objects.all()
    detail = MoviesList.objects.get(pk=pk)
    mname=detail.movie_name
    paginator = Paginator(movies,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'movies':movies,'detail':detail,'cur_user':cur_user,'page_obj':page_obj}
    if not cur_user.watchlist_set.filter(movie_name=mname):
        watch=cur_user.watchlist_set.create(movie_name=detail.movie_name,movie=detail)
        watch.save()
        messages.info(request,"Added_Movie\t"+mname)
    else:
        messages.info(request,"Movie\t"+mname+"\t already in watchlist")   
    return render(request,'Movies/Movielist.html',context)
    
        
        
    
    

def Watchlistview(request):
        cur_user=request.user
        wlist=cur_user.watchlist_set.all()
        context={'wlist':wlist,'cur_user':cur_user}
        return render(request,'Movies/WatchList.html',context)
    


def delWatchlist(request,pk):
    
        cur_user=request.user
        detail=cur_user.watchlist_set.all()
        mov = cur_user.watchlist_set.filter(pk=pk)
        context={'detail':detail,'cur_user':cur_user}
        mov.delete()
        return render(request,'Movies/WatchList.html',context)

def search(request):
    if request.method == 'GET': # this will be GET now      
        movie_name =  request.GET.get('search') # do some research what it does       
        try:
            status = MoviesList.objects.filter(movie_name__icontains=movie_name) # filter returns a list so you might consider skip except part
            return render(request,"Movies/search.html",{"movies":status})
        except:
            return render(request,"Movies/search.html",{'movies':status})
    else:
        return render(request,"search.html",{})
    
        

class MoviesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MoviesList.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class WatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def get_queryset(self, *args, **kwargs):
     return WatchList.objects.all().filter(user=self.request.user)

    def perform_create(self, serializer):
     serializer.save(user=self.request.user)
    

    
    
    



    
    
    
    
    
