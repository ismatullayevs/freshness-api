from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from slugify import slugify


class Category(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_price(self):
        if not self.discount:
            return self.price

        return (self.price * (100 - self.discount)) / 100

    class Meta:
        ordering = ('-modified_at',)
