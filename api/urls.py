from django.urls import path
from .views import create_user, delete_user, list_users, get_user

urlpatterns = [
    path('items/', list_users, name='list_users'),
    path('items/<int:pk>/', get_user, name='get_user'),
    path('items/create/', create_user, name='create_user'),
    path('items/<int:pk>/delete/', delete_user, name='delete_user'),
]
