# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(verbose_name='Product Price', default=0.0, max_digits=11, decimal_places=2),
        ),
    ]
