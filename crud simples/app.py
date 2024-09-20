
lista_de_compras = [] #lista principal


import os #libs necessarias para o projeto
import json


def adicionar(): #função que adiciona o produyo a lista
    produto = input("Digite o item que vc deseja adicionar: ")
    lista_de_compras.append(produto)

def listar(): #função de listar os items da lista
    with open('compras.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        if len(linhas) == 0:
            print('nao ha itens para se listar')
        else:
            print("Items da sua lista de compra")
            for i, linha in enumerate(linhas, start=1):
            
                print(f"{i}. {linha.strip()}")

def remover(): #função de remover items da lista
    item = input("Digite o item que deseja remover: ")
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print("Item removido com sucesso")
    elif len(lista_de_compras) == 0:
        print("nao ha itens para se apagar")
    else:
        print("Nao a item com esse nome")

def salvar_json(): #função que salva a lista em um arquivo json para que nao se perca os dados
    with open('compras.txt', 'w') as file_json:
        json.dumps(lista_de_compras, file_json)

def menu(): #menu principal do projeto
    print("Digite [1] para adicionar")
    print("Digite [2] para remover ")
    print("Digite [3] para listar")



while True: #loop do projeto
    menu()
    escolha  = input("Digite a opção desejada: ")
    escolha_str = str(escolha)
    if escolha == "1":
        os.system('cls')
        adicionar()
        salvar_json()
        print("Item adicionado com sucesso")    
    elif escolha == "2":
        os.system('cls')
        remover()
    elif escolha == "3":
        os.system('cls')
        listar()
    elif escolha == ('sair') or escolha == 'SAIR':
        break
    