from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
from django.core.validators import MinValueValidator
from django.utils.text import slugify
import itertools
from django.urls import reverse

class Category(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("categories", args=[self.slug])

    class Meta:
        ordering=['-title']
        verbose_name="Category"
        verbose_name_plural="Categories"

    def __str__(self):
        return f"{self.title}"


class Worker(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True) 
    photo = models.ImageField(upload_to="worker", blank=True)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', "Female"), ('Prefer not to say', 'Prefer not to say')), default='Prefer not to say')
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=40, choices=(('Available', 'Available'), ('Not Available', 'Not Available')))
    profile_visits = models.IntegerField(default=0)
    # created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name_plural = "Workers"
        verbose_name = "Worker"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name} {self.last_name}")
            slug = base_slug
            for i in itertools.count(1):
                if not Worker.objects.filter(slug=slug).exists():
                    break
                slug = f"{base_slug}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])


