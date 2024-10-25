from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.core import serializers
from .models import Cliente, Carro
import re


def clientes(request: HttpRequest):
    
    if request.method == 'GET':
        clientes_list = Cliente.objects.all()
        return render(request=request, template_name='clientes.html', context={"clientes": clientes_list})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')
        
        cliente = Cliente.objects.filter(cpf=cpf)
        
        context = {'nome': nome, 'sobrenome': sobrenome, 'carros': zip(carros, placas, anos)}
        
        if cliente.exists():
            context['email'] = email
            return render(request=request, template_name='clientes.html', context=context)
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            context['cpf'] = cpf
            return render(request=request, template_name='clientes.html', context=context)
        
        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )
        
        cliente.save()
        
        for carro, placa, ano in list(zip(carros, placas, anos)):
            car = Carro(carro=carro,placa=placa,ano=ano,cliente=cliente)
            car.save()
        
        
        return HttpResponse('teste')

def att_clientes(request: HttpRequest):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    
    cliente_json = serializers.serialize('json', cliente)
    
    return JsonResponse(cliente_json)