# -*- coding: utf-8 -*-
"""calculator.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O44OpqGsJE64sANxhcLPysREg8C_04Qg
"""

number_1 = int(input('Insira o primeiro numero: '))
number_2 = int(input('Insira o segundo numero: '))

#Opções de operações
print("Selecione a operação desejada")
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Potencia')

#Insira a opção
opcao = input("Digite a operação desejada:")

if opcao == '1':
  resultado = number_1 + number_2
  print(f"O resultado da soma é: {resultado}\n")

if opcao == '2':
  resultado = number_1 - number_2
  print(f"O resultado da subtração é: {resultado}\n")

if opcao == '3':
  resultado = number_1 * number_2
  print(f"O resultado da multiplicação é: {resultado}\n")

if opcao == '4':
  resultado = number_1 / number_2
  print(f"O resultado da divisão é: {resultado}\n")

if opcao == '5':
  resultado = number_1 ** number_2
  print(f"O resultado da potencia é: {resultado}\n")

