# Generated by Django 5.0.3 on 2024-06-17 01:52

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('delivered', models.BooleanField(default=False)),
                ('date_purchased', models.DateField(default=datetime.date.today)),
                ('expected_delivery_date', models.DateField(blank=True, null=True)),
                ('date_delivered', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BarInventoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('size', models.PositiveIntegerField()),
                ('refridgerated', models.BooleanField(default=False)),
                ('par_level', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='location.location')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='BarInventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('level', models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('date_expired', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='location.location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.barinventoryproduct')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.IntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='location.location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.barinventoryproduct')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.purchase')),
            ],
        ),
    ]
