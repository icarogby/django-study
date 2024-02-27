from django.urls import path
from appStudy import views

urlpatterns = [
    path('', views.index, name='index'),
]
