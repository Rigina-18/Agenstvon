# Generated by Django 4.2.2 on 2023-09-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='realty',
            name='gmap',
            field=models.TextField(blank=True, null=True),
        ),
    ]
