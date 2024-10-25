from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.clientes, name='clientes'),
    path('atualiza_clientes/', view=views.att_clientes, name='atualiza_clientes')
]