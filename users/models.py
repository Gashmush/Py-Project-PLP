from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from PIL import Image
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)
    is_customer=models.BooleanField(default=False)
    is_worker=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateField(default=timezone.now)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()

    def __str__(self):
        return self.email
    

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="Profile", default="avatar.jpg")
    date_joined=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.photo.path)
        if img.height > 300 or img.width > 300 :
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


