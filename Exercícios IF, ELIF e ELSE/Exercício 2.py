# Questão 02) Faça um programa que pede para o usuário digitar um número inteiro e mostra na tela se o número digitado é positivo, negativo ou neutro.

# Pedindo ao usuário para digitar um número inteiro, utilizando a classe int. 
numero = int(input('Digite um número inteiro: '))

# Utilizando a estrutura condicional IF, ELIF e ELSE para determinar se o número é positivo, negativo ou neutro.   
if numero >= 1:
    # Utilizando o operador de comparação ">=" para a condição retornar verdadeira (True). Caso o número seja maior ou igual (>=) a 1, imprime a mensagem informando que o número é positivo.
    print(f'O número {numero} é um número positivo.')
elif numero < 0:
    # Utilizando o operador de comparação "<" para a condição retornar verdadeira (True). Caso o número seja menor (<) a 0, imprime a mensagem informando que o número é negativo
    print(f'O número {numero} é um número negativo.')
else:
    # Se as condições acima forem falsas (False), retorna verdadeiro (True) e imprime a mensagem informando que é o número é neutro.
    print(f'O número {numero} é um número neutro.')
