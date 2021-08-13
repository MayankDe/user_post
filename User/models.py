from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from datetime import datetime

#Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):       
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password
            )
        
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save( using =self._db)
        return user

    def create_staff(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password
            )
        
        user.is_staff=True

        user.save( using =self._db)
        return user



class User1(AbstractBaseUser):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.EmailField(verbose_name='email' , unique=True,)
    username        = models.CharField(max_length=100,unique=True)
    password        = models.CharField(max_length=100)

    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # Email & Password are required by default.l
    objects= MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Post(models.Model):
    user         =models.ForeignKey(User1, on_delete=models.CASCADE)
    text         = models.TextField()
    created_at = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='last login', auto_now=True)

    def __str__(self):
        return self.text
    