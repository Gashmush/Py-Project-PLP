from django.contrib import admin
from .models import Worker, Category

admin.site.register([Category,Worker])
# Register your models here.
