# Questão 08) Faça um programa que pede para o usuário digitar 10 números inteiros e mostre na tela qual menor número que foi digitado.

# Iniciando uma variável igual a float("inf") chamada "menor" para realizar o menor número percorrendo pela estrutura de repetição FOR.
# 'float("inf")' é infinito. Não existe número maior.
menor = float("inf")
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR com range (alcance) de 1 a 11. O fim (número 11) é exclusivo, então será gerada uma sequência de números de 1 a 10 para verificar o menor número.
for i in range(1,11):
    # Pedindo ao usuário para digitar um número, utilizando a classe float. 
    numeros = float(input(f'Digite o {i}º número: '))
    # Utilizando a estrutura condicional "if" para determinar o menor número.
    # Utilizando o operador de comparação "<" para verificar qual é o menor número digitado.
    if numeros < menor:
        menor = numeros

print(f'O menor número digitado foi: {menor}')