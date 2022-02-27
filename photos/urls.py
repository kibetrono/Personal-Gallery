from django.urls import path,re_path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('search/', views.search, name='search'),
    path('location/<int:image_location>/', views.location, name='location'),
    path('category/<str:pk>/', views.category, name='category'),
]