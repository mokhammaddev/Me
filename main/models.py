from django.core.validators import RegexValidator
from django.db import models


def file_path(instance, filename):
    return f"book/{instance}/{filename}"


def image_path(instance, filename):
    return f"image/{instance}/{filename}"


class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=221)
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=221, null=True, blank=True)
    image = models.ImageField(upload_to=image_path)
    file = models.FileField(upload_to=file_path)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    is_free = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


