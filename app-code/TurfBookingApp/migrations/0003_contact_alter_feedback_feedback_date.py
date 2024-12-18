# Generated by Django 4.2.2 on 2023-06-30 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TurfBookingApp', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 30, 14, 4, 16, 163574), max_length=50),
        ),
    ]
