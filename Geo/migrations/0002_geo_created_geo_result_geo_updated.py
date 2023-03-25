# Generated by Django 4.1.7 on 2023-03-22 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Geo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='geo',
            name='result',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='geo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
