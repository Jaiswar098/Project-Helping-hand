from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='view_profile'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]