# Generated by Django 3.2.3 on 2021-06-29 01:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productreview_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
