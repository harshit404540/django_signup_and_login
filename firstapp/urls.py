from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('login_with_username/',views.login_with_username,name='login_with_username'),
]
