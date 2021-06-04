from django.db import models


class Plan_category(models.Model):

    class Meta:
        verbose_name_plural = 'Plan_categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Plan(models.Model):
    plan_category = models.ForeignKey('Plan_category', null=True, blank=True,
                                      on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Payment_period(models.Model):

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Plan_pricing(models.Model):
    plan = models.ForeignKey('Plan', null=True, blank=True,
                             on_delete=models.SET_NULL)
    payment_period = models.ForeignKey('Payment_period', null=True, blank=True,
                                       on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.price)
