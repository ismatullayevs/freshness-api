from django.db import models
from django.contrib.auth import get_user_model
from products.models import Item
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(max_length=512, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.title + " -> " + str(self.rating)

    class Meta:
        ordering = ('-created_at', '-rating',)
