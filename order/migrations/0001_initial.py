# Generated by Django 5.0.3 on 2024-04-19 21:04

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0001_initial'),
        ('reservation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.FloatField()),
                ('tip', models.FloatField(default=0)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('placed', 'Placed'), ('preparing', 'Preparing'), ('completed', 'completed'), ('canceled', 'Canceled')], default='placed', max_length=10)),
                ('custom_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='reservation.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='order.OrderItem', to='recipe.menuitem'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('method', models.CharField(choices=[('credit', 'Credit'), ('cash', 'Cash'), ('gift', 'Gift'), ('free', 'Free')], default='credit', max_length=10)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('payer_details', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, default='completed', max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='order.payment')),
            ],
        ),
    ]
