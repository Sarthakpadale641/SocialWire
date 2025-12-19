from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('saved/', views.saved_list, name='saved_list'),
    path('history/', views.history_list, name='history_list'),
    path('discover/', views.discover_list, name='discover_list'),
    
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('<int:tweet_id>/save/', views.tweet_save, name='tweet_save'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    
    path('register/', views.register, name='register'),
]


