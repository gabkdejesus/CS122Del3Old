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
                ('agent_no', models.AutoField(primary_key=True, serialize=False)),
                ('agent_first_name', models.CharField(max_length=255, blank=True, null=True)),
                ('agent_last_name', models.CharField(max_length=255, blank=True, null=True)),
                ('total_transactions', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'agent',
            },
        ),
    ]
