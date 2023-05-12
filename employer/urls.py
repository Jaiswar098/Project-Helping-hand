from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='employer_home'),
    path('employer/', views.jobdesc,name='job description'),
    path('applicants/', views.applicants, name='applicants'),
    path('create_job/', views.create_job, name='create_job'),
    path('delete_job/<int:id>', views.delete_job, name='delete_job'),
    path('accept/<int:id>', views.accept, name='accept'),
    path('reject/<int:id>', views.reject, name='reject'),
]