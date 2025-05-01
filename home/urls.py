from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('gravar_comentario/', views.gravar_cmt, name='gravar_comentario')
]


