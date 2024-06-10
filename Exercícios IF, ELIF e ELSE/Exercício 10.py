# Questão 10) Faça um programa que pede 3 números inteiros para o usuário e mostra na tela qual o maior dos três ou se ele são iguais.

# Pedindo ao usuário para digitar três números inteiros, utilizando a classe int. 
numero_um = int(input('Digite o 1º número inteiro: '))
numero_dois = int(input('Digite o 2º número inteiro: '))
numero_tres = int(input('Digite o 3º número inteiro: '))

# Utilizando a estrutura condicional IF, ELIF e ELSE para determinar se o letra é uma vogal, consoante ou outro carácter.
if numero_um > numero_dois and numero_um > numero_tres:
    # Utilizando o operador lógico "and" para a condição retornar verdadeira (True) se ambas as afirmações forem verdadeiras. Caso o número um seja maior (>) que os outros dois, imprime a mensagem informando que o 1º número é o maior.
    print(f'O maior número digitado foi o: {numero_um}')
elif numero_dois > numero_um and numero_dois > numero_tres:
    # Utilizando o operador lógico "and" para a condição retornar verdadeira (True) se ambas as afirmações forem verdadeiras. Caso o número dois seja maior (>) que os outros dois, imprime a mensagem informando que o 2º número é o maior.
    print(f'O maior número digitado foi o: {numero_dois}')
elif numero_tres > numero_um and numero_tres > numero_dois:
    # Utilizando o operador lógico "and" para a condição retornar verdadeira (True) se ambas as afirmações forem verdadeiras. Caso o número três seja maior (>) que os outros dois, imprime a mensagem informando que o 3º número é o maior.
    print(f'O maior número digitado foi o: {numero_tres}')
else:
    # Se a condições acima forem falsas (False), retorna verdadeiro (True) e imprime a mensagem informando que os números são iguais.
    print('Os três números são iguais.')