# Generated by Django 4.2.4 on 2023-08-19 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_Arrival', '0004_feedback_order_details_newarrivals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='num_of_item',
            field=models.IntegerField(),
        ),
    ]