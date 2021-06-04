from django.contrib import admin
from .models import Plan, Plan_pricing, Plan_category, Payment_period


class Plan_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'plan_category',
    )


class Payment_periodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class Plan_pricingAdmin(admin.ModelAdmin):
    list_display = (
        'plan',
        'payment_period',
        'price'
    )

    ordering = ('plan',)


admin.site.register(Plan_category, Plan_categoryAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Payment_period, Payment_periodAdmin)
admin.site.register(Plan_pricing, Plan_pricingAdmin)
