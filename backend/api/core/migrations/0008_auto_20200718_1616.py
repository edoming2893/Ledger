# Generated by Django 3.0.8 on 2020-07-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200717_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_2',
            field=models.CharField(blank=True, max_length=128, verbose_name='address 2'),
        ),
    ]
