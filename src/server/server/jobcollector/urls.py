from django.urls import path
from . import views

urlpatterns = [
    path('get-jobs/', views.get_jobs, name='get_jobs'),
    path('create-job/', views.create_job, name='create_job'),
]