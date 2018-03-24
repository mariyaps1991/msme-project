# Generated by Django 2.0.3 on 2018-03-24 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msme', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msme',
            options={'verbose_name_plural': 'Msme'},
        ),
        migrations.AlterField(
            model_name='msme',
            name='subsidy_provided',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], max_length=8),
        ),
    ]