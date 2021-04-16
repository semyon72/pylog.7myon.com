# Generated by Django 3.1.2 on 2021-01-21 16:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20210119_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entry',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 1, 21), editable=False, verbose_name='create'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='requested',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 18, 6, 19, 780422), editable=False, verbose_name='registration was requested'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]