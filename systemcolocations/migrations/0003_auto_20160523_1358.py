# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemcolocations', '0002_auto_20160523_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desempleado',
            name='fechaNacimiento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
