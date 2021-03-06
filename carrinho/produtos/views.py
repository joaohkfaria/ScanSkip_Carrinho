# -*- coding: utf-8 -*-
from django.shortcuts import render
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/utils/')
from utils.network import Network
from django.http import JsonResponse


def produto(request, idProduto):
    urlProduto = 'https://scan-skip-plu-teste.herokuapp.com/produto/' + idProduto
    network = Network()
    response = network.request(urlProduto, 'GET')
    if response != -1:
        quantidade = 1
        nome = response['nome']
        marca = response['marca']
        preco = response['valor']
        preco = ('%.2f' % (float(preco)/100)).replace('.', ',')
        categoria = response['categoria']
        imagem = response['imagem']

        # Salvando ultimo produto escaneado na sessão
        request.session['lastScannedProduct'] = idProduto

        return render(request, 'produto-escaneado-confirmacao.html', {'idProduto': idProduto, 'nome': nome, 'marca': marca, 'preco': preco, 'categoria': categoria, 'imagem': imagem, 'quantidade': quantidade, 'registrado': True})
    else:
        nome = 'Produto não registrado'
        marca = '-------'
        preco = '-------'
        categoria = '-------'
        return render(request, 'produto-escaneado-confirmacao.html', {'idProduto': idProduto, 'nome': nome, 'marca': marca, 'preco': preco, 'categoria': categoria, 'registrado': False})


def testeProduto(request):
    dicionario = {'idProduto': '12', 'nome': 'Agua', 'valor': '499', 'marca': 'Cristal', 'categoria': 'Consumo', 'imagem': 'http://charges.uol.com.br/upload/bobagens/aguad.jpg'}
    return JsonResponse(dicionario)
