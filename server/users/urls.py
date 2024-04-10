from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='reg'),
    path('login/', views.loginUser, name='log'),
    path('logout/', views.logoutUser, name='logout')
]