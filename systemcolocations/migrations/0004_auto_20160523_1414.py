# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemcolocations', '0003_auto_20160523_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oferta',
            old_name='idempresa',
            new_name='nombreempresa',
        ),
    ]
