# Questão 07) Faça um programa que pede para o usuário digitar 10 números inteiros e mostre na tela qual maior número que foi digitado.

# Iniciando uma variável igual a 0 chamada "maior" para realizar o maior número percorrendo pela estrutura de repetição FOR.
maior = 0
# Utilizando o operador de associação "in" e a estrutura de repetição FOR com range (alcance) de 1 a 11. O fim (número 11) é exclusivo, então será gerada uma sequência de números de 1 a 10 para verificar o maior número.
for i in range(1,11):
    # Pedindo ao usuário para digitar um número, utilizando a classe float. 
    numeros = float(input(f'Digite o {i}º número: '))
    # Utilizando a estrutura condicional "if" para determinar o maior número.
    # Utilizando o operador de comparação ">" para comparar cada número digitado na variável "numeros" com o variável "maior"
    if numeros > maior:
        maior = numeros

print(f'O maior número digitado foi: {maior}')