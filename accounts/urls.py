from django.urls import path
from . import views

urlpatterns=[
    path('',views.RegisterAdmin,name=''),
    path('Login',views.Login,name='Login'),
    path('logout',views.Logout,name='logout')
]