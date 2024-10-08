# Generated by Django 5.1 on 2024-09-25 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_by', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_service', to='business.services')),
            ],
            options={
                'verbose_name_plural': 'BOOKINGS',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_by', to=settings.AUTH_USER_MODEL)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salon_review', to='business.salons')),
            ],
            options={
                'verbose_name_plural': 'REVIEWS',
            },
        ),
    ]
