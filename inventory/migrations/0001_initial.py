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
                ('date_purchased', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BarInventoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('refridgerated', models.BooleanField(default=False)),
                ('par_level', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='location.location')),
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
                ('quantity', models.IntegerField(default=1)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='location.location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.barinventoryproduct')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.purchase')),
            ],
        ),
    ]
