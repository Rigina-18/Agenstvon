# Generated by Django 4.2.1 on 2023-06-03 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_manager_realty_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.manager'),
        ),
    ]
