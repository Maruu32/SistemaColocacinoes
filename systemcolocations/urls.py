from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home_view),
    url(r'^/desempleados$', views.desempleados_view),
    url(r'^/ofertas$', views.ofertas_view),
    url(r'^/empresas$', views.empresas_view),
]