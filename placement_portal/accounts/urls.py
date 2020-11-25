from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerView, name = 'register'),
    path('login/', views.loginView, name = 'login'),
    path('', views.homeView, name = 'home'),
    path('logout/', views.logoutView, name = 'logout'),
    path('notices/', views.noticeView, name = 'notices'),
    path('apply/<str:jobId>/', views.applyToJobView, name = 'apply'),
    path('applications/', views.applicantView, name = 'applications')


    
]
