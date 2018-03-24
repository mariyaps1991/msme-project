# Generated by Django 2.0.3 on 2018-03-24 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msme', '0002_auto_20180325_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msme',
            name='pan_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{9}$')]),
        ),
    ]
