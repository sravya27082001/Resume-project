
from django.urls import path
from .import views

urlpatterns=[
    path('resumefill', views.resumeFill, name='resume_fill'),
    path('resumeview', views.resumeView, name='resume_view'),
]
