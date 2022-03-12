import email
from django.db import models

# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey('UserManagement.User', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    phone_number = models.PositiveBigIntegerField()
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.name 