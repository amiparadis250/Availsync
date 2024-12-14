import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom manager for user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Create and return a regular user with a username and password.
        """
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Create and return a superuser with a username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.EmailField(unique=True)  # username is email
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    profile_image = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=20)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager() 
    
    USERNAME_FIELD = 'username'  
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']  
    
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'


# Institution model
class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    username = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    totalstuffs = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bio = models.CharField(max_length=200)
    working_days = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)

    class Meta:
        db_table = 'institutions'


class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    profile_image = models.CharField(max_length=200)
    role = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    workdescription = models.CharField(max_length=200)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Updated to use custom user model

    class Meta:
        db_table = 'staffs'
