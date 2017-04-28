# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('agent_first_name', models.CharField(verbose_name='First Name', max_length=200, default='John')),
                ('agent_last_name', models.CharField(verbose_name='Last Name', max_length=200, default='Smith')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(verbose_name='Product Name', max_length=200, default='product name'),
        ),
    ]
