from django.urls import path
from base.views import user_login,signup,logout
from django.urls import include
from django.contrib.auth.views import LogoutView
from base import views

urlpatterns = [
path('login/', user_login, name='login'),
path('signup/', signup, name='signup'),
path('logout/', logout, name='logout'),

]   