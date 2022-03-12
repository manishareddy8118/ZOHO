from django.urls import path
app_name = "Contacts"
from Contacts.views import *

urlpatterns = [
    path('', Contacts, name='home')
]