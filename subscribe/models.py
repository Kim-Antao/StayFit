import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from plan.models import Plan, Plan_category


gender_options = [
    ("female", "fe"),
    ("male", "ma"),
]


class Subscriber(models.Model):
    plan_category = models.ForeignKey(Plan_category, null=False, blank=False, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, null=False, blank=False, on_delete=models.CASCADE)
    subscription_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False,
                              validators=[MinValueValidator(18),
                                          MaxValueValidator(70)])
    height = models.DecimalField(max_digits=4, decimal_places=2, null=False,
                                 blank=False, validators=[MinValueValidator(18),
                                                          MaxValueValidator(70)])
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=False,
                                 blank=False, validators=[MinValueValidator(18),
                                                          MaxValueValidator(70)])
    gender = models.CharField(max_length=10, choices=gender_options)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.subscription_number
