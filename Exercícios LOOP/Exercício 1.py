# Questão 01) Faça um programa que pede 1 número inteiro entre 1 e 10 para o usuário e mostre na tela a tabuada desse número.

# Pedindo ao usuário para digitar um número inteiro e positivo, utilizando a classe int. 
numero_inteiro = int(input('Digite um número inteiro entre 1 e 10: '))

# Utilizando o operador de associação "in" a estrutura de repetição FOR com range (alcance) de 1 a 11. O fim (número 11) é exclusivo, então será gerada uma sequência de números de 1 a 10.
for i in range(1,11):
    # Percorrendo o loop de 1 a 10, multiplicando a variável "numero_inteiro" pelo valor atual de "i" e mostrando na tela número por número para ser realizada a multiplicação da tabuada.
    print(f'{numero_inteiro} x {i}: {numero_inteiro * i}')

