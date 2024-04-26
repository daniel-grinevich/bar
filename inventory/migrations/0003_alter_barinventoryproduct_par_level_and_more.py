# Generated by Django 5.0.3 on 2024-04-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_barinventoryproduct_created_at_purchase_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barinventoryproduct',
            name='par_level',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='barinventoryproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='barinventoryproduct',
            name='size',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]