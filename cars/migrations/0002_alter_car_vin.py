# Generated by Django 4.0.5 on 2022-06-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Vin'),
        ),
    ]
