# Generated by Django 2.0.3 on 2018-03-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msme', '0003_auto_20180325_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msme',
            name='bank_name',
            field=models.CharField(choices=[('STATE BANK OF INDIA', 'State Bank of India'), ('HDFC BANK', 'HDFC'), ('INDIAN BANK', 'Indian Bank')], max_length=50),
        ),
    ]
