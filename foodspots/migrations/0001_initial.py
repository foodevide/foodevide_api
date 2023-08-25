# Generated by Django 4.1.3 on 2023-08-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodSpot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='foodspot_images/')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('time', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('categories', models.ManyToManyField(to='foodspots.category')),
            ],
        ),
    ]
