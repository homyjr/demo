from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:artist_id>/', views.dummy, name = 'dummy'),
    path('create/', views.create_song, name='create'),
]