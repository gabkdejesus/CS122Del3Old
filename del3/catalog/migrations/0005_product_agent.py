# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
        ('catalog', '0004_delete_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='agent',
            field=models.ForeignKey(default=1, to='agents.Agent'),
        ),
    ]
