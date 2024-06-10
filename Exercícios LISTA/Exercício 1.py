# Questão 01) Crie uma lista chamada números, peça para o usuário inserir 5 números e alimente essa lista, depois mostre todos os números na tela de forma separada.

# Criando uma lista vazia para armazenar os números.
lista_numeros = []
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR com range (alcance) de 1 a 6. O fim (número 6) é exclusivo, então será gerada uma sequência de números de 1 a 5 para o usuário digitar 5 números.
for i in range(1,6):
    # Pedindo ao usuário para digitar um número, utilizando a classe float. 
    numeros = float(input(f'Digite o {i}º número: '))
    # Utilizando o método "append" para adicionar os números digitados pelo usuário ao final da lista "lista_numeros".
    lista_numeros.append(numeros)

# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a lista e imprimir os números digitados pelo usuário de forma separada.
for lista in lista_numeros:
    print(lista)

