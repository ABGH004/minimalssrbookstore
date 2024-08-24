# Generated by Django 5.1 on 2024-08-24 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='identity_code',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(),
        ),
    ]
