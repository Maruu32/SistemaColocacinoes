from django.db import models

class Areas(models.Model):
    areasTrabajo = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s' % (self.areasTrabajo)


class TipoTrabajo(models.Model):
    trabajo = models.CharField(max_length=30)
    area = models.ForeignKey('Areas')

    def __unicode__(self):
        return '%s' % (self.trabajo)


class Desempleado(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=50, null=True)
    fechaNacimiento = models.DateField(blank=True, null=True)
    trabajo = models.ForeignKey('TipoTrabajo')


    def __unicode__(self):
        return '%s %s' % (self.nombre, self.apellido)


class Empresa(models.Model):
    nombreEmpresa = models.CharField(max_length=50, blank=True, null=True)
    ciudad= models.CharField(max_length=30)


    def __unicode__(self):
        return '%s' % (self.nombreEmpresa)


class Oferta(models.Model):
    nombreempresa = models.ForeignKey('Empresa')
    area = models.ForeignKey('Areas')
    descripcion = models.CharField(max_length=140)
    tipodetrabajo = models.ForeignKey('TipoTrabajo')

    def __unicode__(self):
        return '%s' % (self.descripcion)