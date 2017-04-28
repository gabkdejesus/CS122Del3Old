# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
    ]
