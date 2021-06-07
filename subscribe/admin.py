from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):

    def payment_plan(self, obj):
        return (obj.plan_pricing.payment_period)

    readonly_fields = ('subscription_number', 'date',
                       )

    fields = ('subscription_number', 'plan', 'plan_pricing', 'date', 'full_name',
              'age', 'height', 'weight', 'gender', 'email',
              'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1',
              'street_address2', 'county', )

    list_display = ('subscription_number', 'date', 'full_name',
                    'payment_plan',)

    ordering = ('-date',)


admin.site.register(Subscriber, SubscriberAdmin)
