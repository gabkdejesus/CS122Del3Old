# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_no', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255, blank=True, null=True)),
                ('color', models.CharField(max_length=255, blank=True, null=True)),
                ('quantity_stocked', models.IntegerField(blank=True, null=True)),
                ('personalization_limit', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
