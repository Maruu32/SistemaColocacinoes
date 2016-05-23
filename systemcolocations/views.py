from django.shortcuts import render
from .models import *


def home_view(request):
    return render(request, 'home.html', {})


def desempleados_view(request):
    desempleados = Desempleado.objects.all()
    return render(request, 'desempleados.html', {'desempleados': desempleados})


def ofertas_view(request):
    ofertas = Oferta.objects.all()
    desempleados = Desempleado.objects.all()
    return render(request, 'ofertas.html',
        {
            'ofertas_objects': ofertas,
            'desempleados_objects' : desempleados})


def empresas_view(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas.html', {'empresas': empresas})