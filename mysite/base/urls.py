from django.urls import path
from base import views
from django.urls import include

urlpatterns = [
path('login/', views.login, name='login'),
path('signup/', views.signup, name='signup'),
]