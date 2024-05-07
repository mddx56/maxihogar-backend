import uuid
from django.db import models


class Categorie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=355, null=False)
    description = models.TextField(null=True, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Sub_Categorie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    parent = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=355, null=False)
    description = models.TextField(null=True, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=355, null=False)
    description = models.TextField(null=True, blank=True, default="")
    summary = models.CharField(max_length=500, null=True, blank=True, default="")
    cover = models.CharField(max_length=500, blank=True, null=True, default="")
    category = models.ForeignKey(Sub_Categorie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product_Attribute(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    types = models.TextField()
    value = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.types


class Product_Sku(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_attribute = models.ForeignKey(
        Product_Attribute, on_delete=models.CASCADE, related_name="size"
    )
    color_attribute = models.ForeignKey(
        Product_Attribute, on_delete=models.CASCADE, related_name="color"
    )
    sku = models.CharField(max_length=450)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.sku


class Product_Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.image.url
