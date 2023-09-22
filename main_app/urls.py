from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name= 'home'),
path('about/', views.about, name='about'),
path('all_finch/', views.all_finch, name='all_finch'),
]
