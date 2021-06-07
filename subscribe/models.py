import uuid
import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField

from datetime import date
from plan.models import Plan, Plan_pricing


gender_options = [
    ("female", "Female"),
    ("male", "Male"),
]


class Subscriber(models.Model):
    plan_pricing = models.ForeignKey(Plan_pricing, null=False, blank=False, on_delete=models.CASCADE)
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
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    paid_until = models.DateTimeField(null=True, blank=True)
    """
    check to see if the date is of correct format
    """
    def set_paid_until(self, date_or_timestamp):
        if isinstance(date_or_timestamp, int):
            paid_until = date.fromtimestamp(date_or_timestamp)
        elif isinstance(date_or_timestamp, str):
            paid_until = date.fromtimestamp(int(date_or_timestamp))
        else:
            paid_until = date_or_timestamp

        self.paid_until = paid_until
        self.save()

    def has_paid(self, current_date=datetime.date.today()):
        if self.paid_until is None:
            return False
        return current_date < self.paid_until

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.subscription_number
