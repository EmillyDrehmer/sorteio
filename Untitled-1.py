#Crie um programa que:
#1. Peça ao usuário:
#Quantos números deseja sortear(feito)
#2. Gere números aleatórios entre 1 e 100(feito)
#3. Armazene os números em uma lista(feito)
#4. Mostre:Lista de números sorteados(feito)

#Maior número(feito)
#Menor número(feito)
#Média dos números(feito)
#Raiz quadrada da média (usar math.sqrt)(feito)
#. Mostre a data e hora atual do sorteio(feito)

import random

import math

import datetime



while True:  # Loop principal do programa
     
 def cab():
    mensagem = "Bem Vindo!!"
    tam = len(mensagem)
    print("="*(tam*2))
    print(mensagem.center(tam*2))
    print("="*(tam*2))

 cab()

 qtd = int(input("\nQuantos numeros deseja sortear?"))

 nums = []

 for i in range(qtd):
    num = random.randint(1, 100)
    nums.append(num)

 print("\nNúmeros sorteados:", nums)


 def maior():#Função para achar o maior valor da lista
    return max(nums)

 print("\nO maior valor sorteado é:", maior())

 def menor(): #Função para encontar o menor valor da lista
    return min(nums)

 print("\no menor valor sorteado é:", menor())

 def media(): #Função para calcular a média dos registros inseridos
    return sum(nums) / len(nums)

 print("\nA media dos valores sorteados é:",media())

 if media() >= 0:
    media = sum(nums) / len(nums)
    raiz_media = math.sqrt(media)
    print("\nA raiz quadrada da media é:", raiz_media)
 else:
    print("\nNão existe raiz quadrada real de número negativo.")


 dt_sort = datetime.datetime.now()


 print("\nData do sorteio:", dt_sort)


 nums.sort()
 print("\nNumeros sorteados ordenados:",nums)







 nsort = input("\nDeseja realizar um novo sorteio? (s/n): ").lower()

 if nsort != 's':
        print("Programa encerrado.\n" "Obrigada pela preferência! ")
        break