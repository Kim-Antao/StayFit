from django.contrib import admin
from .models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'title',
        'content',
        'stars'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
