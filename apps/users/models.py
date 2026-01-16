from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Email обязателен")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Email обязателен")
        
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser должен иметь is_staff=True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser должен иметь is_superuser=True")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user
    

class User(AbstractUser):
    username = None
    last_name = None
    email = models.EmailField(unique=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def get_short_name(self):
        if self.first_name:
            return self.first_name
        
        return self.email

    def __str__(self):
        return self.email
