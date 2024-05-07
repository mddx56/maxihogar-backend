import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product

User = get_user_model()


def user_directory_path(instance, filename):
    return "users/{0}/{1}".format(instance.user.username, filename)


class Profile(models.Model):
    GENDER_MALE = "m"
    GENDER_FEMALE = "f"
    OTHER = "o"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (OTHER, "Other"),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    ci = models.CharField(max_length=9, default="")
    avatar = models.CharField(blank=True, null=True, default="", max_length=450)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True)
    phone_number = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    about = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Wishlist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
