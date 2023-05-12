from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contactUs',views.contactus, name='contactus'),
    path('about',views.about, name='about'),
    path('index',views.index, name='index'),
    path('job/<int:id>', views.job, name='job'),
    path('apply/<int:id>', views.apply_job, name='apply'),
]