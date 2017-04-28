# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170427_1418'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agent',
        ),
    ]
