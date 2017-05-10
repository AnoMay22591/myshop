# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170430_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order_user'),
        ),
    ]