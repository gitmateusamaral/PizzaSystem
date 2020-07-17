# -*- coding: utf-8 -*-
"""
1 - Menu:
    Comprar Pizza
    Sair
    
2 - Escolher 5 ingredientes. P.ex. massa, queijo, recheios.
    Med) O usuário escolhe apenas 1 de cada tipo de ingrediente. 
         Ingredientes obrigatórios e opcionais. Cada ingrediente tem seu preço.            
    Hard) Alguns ingredientes podem ser escolhidos mais de uma vez

3 - Exibir a pizza, o custo e pedir confirmação:
    Descartada
    Solicitar endereço e método de pagamento
    
    God) Cada ingrediente possui um estoque associado
    MofU) Cada usuário pode comprar mais de uma pizza

Aluno: Mateus Amaral do Nascimento(181101036)
"""

def menu():
    comprar = str(input("Iniciar montagem de pizza?(s/n): ")).lower().strip()
    estoque_inicial = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    if comprar == "s":
        print("Processo de montagem iniciando...")
        montagem(0,[],estoque_inicial)
    elif comprar == "n":
        print("Pedido de pizza cancelado!")
    else: 
        print("Comando inválido!")
    
def montagem(preco_total, lista_pizza, estoque):
    #Tupla:
    ingredientes = ("massa tradicional", "massa fina", "mussarela", "parmesão", "calabresa", "presunto", "ovo", "azeitona", "bacon", "tomate")
    preco_ingrediente = (0, 5, 5, 5, 5, 5, 5, 5, 10, 5)
    n_ingredientes = 5
    preco_pizza = 0
    pizza = []
    massa_escolhida = False
    
    print(f"\nEscolha {n_ingredientes} ingredientes: \n{ingredientes[0]}|estoque: {estoque[0]} \n{ingredientes[1]}|estoque: {estoque[1]} \n{ingredientes[2]}|estoque: {estoque[2]} \n{ingredientes[3]}|estoque: {estoque[3]} \n{ingredientes[4]}|estoque: {estoque[4]} \n{ingredientes[5]}|estoque: {estoque[5]} \n{ingredientes[6]}|estoque: {estoque[6]} \n{ingredientes[7]}|estoque: {estoque[7]} \n{ingredientes[8]}|estoque: {estoque[8]} \n{ingredientes[9]}|estoque: {estoque[9]} \n\nÉ NECESSÁRIO ESCOLHER A MASSA PRIMEIRO!!!")
    
    while n_ingredientes > 0:
        ingrediente_escolhido = str(input("Escreva um dos ingredientes apresentados para adicionar ele na pizza: ")).lower().strip()
        
        if ingrediente_escolhido in ingredientes and massa_escolhida == True and ingrediente_escolhido != "massa tradicional" and ingrediente_escolhido != "massa fina" and estoque[ingredientes.index(ingrediente_escolhido)] > 0:
            estoque, pizza, preco_pizza, n_ingredientes = controlador(estoque, ingredientes, pizza, preco_pizza,preco_ingrediente,ingrediente_escolhido, n_ingredientes)
            print(estoque)
        elif ingrediente_escolhido in ingredientes and massa_escolhida == True and (ingrediente_escolhido == "massa tradicional" or ingrediente_escolhido == "massa fina") and massa_escolhida == True:
            print("A massa já foi escolhida!") 
        elif massa_escolhida == True:
            print("Ingrediente inexistente ou fora de estoque!")
        elif (ingrediente_escolhido == "massa tradicional" or ingrediente_escolhido == "massa fina") and massa_escolhida == False and estoque[ingredientes.index(ingrediente_escolhido)] > 0:
            estoque, pizza, preco_pizza, n_ingredientes = controlador(estoque, ingredientes, pizza, preco_pizza, preco_ingrediente, ingrediente_escolhido, n_ingredientes)
            massa_escolhida = True
            print(estoque)
        elif (ingrediente_escolhido == "massa tradicional" or ingrediente_escolhido == "massa fina") and estoque[ingredientes.index(ingrediente_escolhido)] <= 0:
            print("Massa fora de estoque!")
        elif massa_escolhida == False:
            print("O primeiro ingrediente escolhido deve ser a massa! Ela é um ingrediente obrigatório!")
        
    print(f"\nPizza pronta, ingredientes escolhidos: {pizza[0]} com cobertura de {pizza[1]}, {pizza[2]}, {pizza[3]} e {pizza[4]} \nPreço da pizza: R${preco_pizza}")
    lista_pizza.append(pizza)
    preco_total += preco_pizza
    finalizar(preco_total, lista_pizza, estoque)

    
def controlador(estoque, ingredientes, pizza, preco_pizza, preco_ingrediente, ingrediente_escolhido, n_ingredientes):
    estoque[ingredientes.index(ingrediente_escolhido)] -= 1
    pizza.append(ingrediente_escolhido)
    preco_pizza += preco_ingrediente[ingredientes.index(ingrediente_escolhido)]
    n_ingredientes -= 1
    return estoque, pizza, preco_pizza, n_ingredientes


def finalizar(preco_total, lista_pizza, estoque):
    repetir_processo = str(input("Deseja adicionar outra pizza?(s/n): ")).lower().strip()
    if repetir_processo == "s":
        montagem(preco_total, lista_pizza,estoque)
    elif repetir_processo == "n":
        endereco = str(input("Digite seu endereço: "))
        pagamento = str(input("Qual o método de pagamento? "))
        print("\n-------------------------------------------- \nAs pizzas escolhidas são:")
        for i in range(len(lista_pizza)):
            print(f"\nPizza {i+1}: {lista_pizza[i][0]} com cobertura de {lista_pizza[i][1]}, {lista_pizza[i][2]}, {lista_pizza[i][3]} e {lista_pizza[i][4]}")
        print(f"\nO pedido será entregue em {endereco} \nO método de pagamento escolhido é {pagamento} \nO preço final do pedido é R${preco_total}")
        confirmar()
    else: 
        print("Comando inválido!")

def confirmar():
        confirmar = str(input("Podemos confirmar o pedido?(s/n): ")).lower().strip()
        if confirmar == "s":
            print("\nPedido de compra finalizado! \nObrigado por comprar com a gente!!!")
        else:
            print("Pedido cancelado!")


