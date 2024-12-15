from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.Register, name='register'),
    path('availabilitychecker/', views.Checker, name='availabilitychecker'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('dashboard/staff/', views.admin_staffs, name='adminstaff'),
    path('dashboard/users/', views.admin_users, name='adminusers'),
    path('dashboard/institutions/', views.admin_Institutions, name='adminInstitutions'),
    
]