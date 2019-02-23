# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('play/', views.play),
    path('layout/', views.layout),
    path('play2/', views.play2),
    path('phy/profile/', views.my_profile),
    path('event/', views.event),
    path('fail/', views.fail),
    path('help/', views.help),
    path('warn/', views.warn),
    path('', views.newsfeed),
    path('feed/<pk>/', views.detail_feed),
    path('pages/', views.pages),
    path('new/', views.new_feed),
    path('feed/<pk>/remove/', views.remove_feed),
    path('feed/<pk>/edit/', views.edit_feed),
    path('pages/new/', views.new_page),
]
