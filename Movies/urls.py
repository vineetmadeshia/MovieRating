from django.urls import path
from . import views

#app_name='Movies'
urlpatterns=[path('',views.loginPage,name='login'),
             path('home/logout',views.logoutUser,name='logout'),
             path('home/',views.home,name='home'),
             path('home/<int:pk>',views.Moviedetail,name='moviedetail'),
             path('home/search/',views.search,name='search'),
             path('watchlist/',views.Watchlistview,name='watchlistview'),
             path('watchlist/<int:pk>/',views.Watchlist,name='watchlist'),
             path('moviedelete/<int:pk>',views.delWatchlist,name='delwatch'),
             path('register/',views.registerPage,name='register'),
             ]
