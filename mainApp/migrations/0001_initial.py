# Generated by Django 3.1.7 on 2021-03-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('phone', models.CharField(default=None, max_length=20, null=True)),
                ('bankName', models.EmailField(blank=True, default=None, max_length=20, null=True)),
                ('ifscCode', models.EmailField(blank=True, default=None, max_length=20, null=True)),
                ('accountNumber', models.EmailField(blank=True, default=None, max_length=20, null=True)),
                ('total', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
