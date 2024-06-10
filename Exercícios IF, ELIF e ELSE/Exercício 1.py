# Questão 01) Faça um programa que pede 2 números inteiros para o usuário e mostre na tela qual o maior dos dois ou se ele são iguais.

# Pedindo ao usuário para digitar dois números inteiros, utilizando a classe int. 
numero_um = int(input('Digite o 1º número inteiro: '))
numero_dois = int(input('Digite o 2º número inteiro: '))

# Utilizando a estrutura condicional IF, ELIF e ELSE para determinar qual é o maior número ou se os números são iguais.
if numero_um > numero_dois:
    # O operador de comparação ">" para verificar se o número é maior que o outro.
    print(f'O maior número é o: {numero_um}')
elif numero_dois > numero_um:
    print(f'O maior número é o: {numero_dois}')
else:
    print(f'Os números são iguais.')
