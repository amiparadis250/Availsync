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
    path('dashboard/<str:user_id>/', views.dashboard_staffs, name='StaffDashboard'),
    path('dashboard/availability/<str:user_id>/', views.availability_staffs, name='availability_staffs'),
    path('dashboard/staff/<str:user_id>/', views.Workmates, name='workmates'),
    path('dashboard/institution/<str:user_id>/', views.Institution_staff, name='Institution_staff'),
    
]