# Generated by Django 3.0.8 on 2020-07-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200727_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_start',
            field=models.TimeField(max_length=50),
        ),
    ]
