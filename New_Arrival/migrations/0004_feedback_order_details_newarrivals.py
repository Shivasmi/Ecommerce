# Generated by Django 4.2.4 on 2023-08-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_Arrival', '0003_alter_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=100)),
                ('num_of_item', models.IntegerField(max_length=50)),
                ('total_summary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='NewArrivals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('descriptions', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_new_arrival', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='newarrival_images/')),
                ('categories', models.ManyToManyField(to='New_Arrival.newarrivals')),
            ],
        ),
    ]