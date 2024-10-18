# Generated by Django 4.2.2 on 2023-06-29 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Turf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turf_name', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('charges', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.CharField(max_length=50)),
                ('for_date', models.CharField(max_length=50)),
                ('for_time', models.CharField(max_length=50)),
                ('charges', models.IntegerField()),
                ('card_no', models.CharField(max_length=20)),
                ('card_holder', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TurfBookingApp.customer')),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TurfBookingApp.turf')),
            ],
        ),
    ]
