# Generated by Django 3.2.3 on 2021-06-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0004_alter_subscriber_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='paid_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]