# Generated by Django 3.1.7 on 2021-03-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0021_remove_checkout_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='mode',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
