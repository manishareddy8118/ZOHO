from django.urls import path
app_name = "UserManagement"
from UserManagement.views import *

urlpatterns = [
    path('signin/', UserLogin, name="login"),
    path('signup/', UserRegister, name="register"),
    path('logout/', UserLogout, name="logout")
]