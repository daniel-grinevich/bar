# Generated by Django 5.0.3 on 2024-04-03 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barinventoryitem',
            name='date_purchased',
        ),
        migrations.RemoveField(
            model_name='barinventoryitem',
            name='purchase',
        ),
        migrations.RemoveField(
            model_name='barinventoryitem',
            name='purchase_price',
        ),
        migrations.AddField(
            model_name='barinventoryproduct',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='location.location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='barinventoryproduct',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.IntegerField()),
                ('date_purchased', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.barinventoryproduct')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.purchase')),
            ],
        ),
    ]