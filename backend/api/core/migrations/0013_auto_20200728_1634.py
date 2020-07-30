# Generated by Django 3.0.8 on 2020-07-28 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200728_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time_start',
        ),
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.CharField(choices=[('1', '7:00am'), ('2', '8:00am'), ('3', '9:00am'), ('4', '10:00am'), ('5', '11:00am'), ('6', '12:00pm'), ('7', '1:00pm'), ('8', '2:00pm'), ('9', '3:00pm'), ('10', '4:00pm'), ('11', '5:00pm')], default='Choose End Time', max_length=50),
        ),
        migrations.AddField(
            model_name='appointment',
            name='location',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_time',
            field=models.CharField(choices=[('1', '7:00am'), ('2', '8:00am'), ('3', '9:00am'), ('4', '10:00am'), ('5', '11:00am'), ('6', '12:00pm'), ('7', '1:00pm'), ('8', '2:00pm'), ('9', '3:00pm'), ('10', '4:00pm'), ('11', '5:00pm')], default='Choose Start Time', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=64, verbose_name='city'),
        ),
    ]