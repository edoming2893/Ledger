# Generated by Django 3.0.8 on 2020-07-16 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('registration_date', models.DateTimeField(verbose_name='date-registered')),
                ('work', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('registration_date', models.DateTimeField(verbose_name='date-registered')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Doctor')),
            ],
        ),
    ]
