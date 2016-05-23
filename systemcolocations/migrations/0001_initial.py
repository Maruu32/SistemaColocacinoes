# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('areasTrabajo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Desempleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dnipasaporte', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreEmpresa', models.CharField(max_length=50, null=True, blank=True)),
                ('razonsocial', models.CharField(max_length=30)),
                ('cuil', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=140)),
                ('area', models.ForeignKey(to='systemcolocations.Areas')),
                ('idempresa', models.ForeignKey(to='systemcolocations.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='TipoTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trabajo', models.CharField(max_length=30)),
                ('area', models.ForeignKey(to='systemcolocations.Areas')),
            ],
        ),
        migrations.AddField(
            model_name='oferta',
            name='tipodetrabajo',
            field=models.ForeignKey(to='systemcolocations.TipoTrabajo'),
        ),
        migrations.AddField(
            model_name='desempleado',
            name='trabajo',
            field=models.ForeignKey(to='systemcolocations.TipoTrabajo'),
        ),
    ]
