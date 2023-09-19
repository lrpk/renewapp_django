from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to="photos/categories", blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])  # повертає slug name категорії продукту
        # (використовується в navbar.html для функціонування посилань категорій)


