# Generated by Django 5.0.3 on 2024-03-21 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('chairs', models.IntegerField(verbose_name='number of chairs at a table')),
                ('available', models.BooleanField(default=True)),
                ('style', models.CharField(choices=[('bar', 'Bar Table'), ('indoor', 'Indoor Table'), ('outdoor', 'Outdoor Table')], max_length=20)),
                ('locatoin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='location.location')),
            ],
        ),
    ]
