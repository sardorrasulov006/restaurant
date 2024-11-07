# Generated by Django 5.1.2 on 2024-10-10 21:40

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('number_of_people', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manzili', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=90, scale=None, size=[800, 600], upload_to='images')),
            ],
        ),
    ]