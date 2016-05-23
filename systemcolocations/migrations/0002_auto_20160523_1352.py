# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemcolocations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='cuil',
            new_name='ciudad',
        ),
        migrations.RemoveField(
            model_name='desempleado',
            name='dnipasaporte',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='razonsocial',
        ),
        migrations.AddField(
            model_name='desempleado',
            name='dni',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
