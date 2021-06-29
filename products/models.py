from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        total = 0
        if self.reviews.count() > 0:
            for review in self.reviews.values():
                total = total + int(review['stars'])
            count = self.reviews.count()
            total = total/count
        return total


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField(validators=[MinValueValidator(0),
                                MaxValueValidator(5)])

    def __str__(self):
        return self.title
