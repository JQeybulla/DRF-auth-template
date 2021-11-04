from django.urls import path
from .views import UsersList
from .views import MultiTen


urlpatterns = [
    path('users/', UsersList.as_view(), name='users_list'),

    path('add/', MultiTen.as_view(), name='testinc_celery'),
]