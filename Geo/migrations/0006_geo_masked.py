# Generated by Django 4.1.7 on 2023-03-25 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Geo', '0005_alter_geo_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='geo',
            name='masked',
            field=models.ImageField(default=1, upload_to='results'),
            preserve_default=False,
        ),
    ]
