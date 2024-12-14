from django.urls import path
from . import views

urlpatterns = [
     path('', views.hello, name='home'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.Register, name='register'),
    
]