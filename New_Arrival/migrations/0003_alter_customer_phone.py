# Generated by Django 4.2.4 on 2023-08-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_Arrival', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(),
        ),
    ]