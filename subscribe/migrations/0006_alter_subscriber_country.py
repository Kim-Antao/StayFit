# Generated by Django 3.2.3 on 2021-06-07 21:09

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0005_subscriber_paid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
