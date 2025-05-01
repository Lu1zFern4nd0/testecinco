from django.urls import path
from . import views
urlpatterns = [
    path('', views.bombom, name='bombom'),
]