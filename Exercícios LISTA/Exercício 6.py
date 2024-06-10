# Questão 06) Crie uma lista chamada números, peça para o usuário inserir 5 números e alimente essa lista, depois mostre o menor número dessa lista.

# Criando uma lista vazia para armazenar os números.
lista_numeros = []
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR com range (alcance) de 1 a 6. O fim (número 6) é exclusivo, então será gerada uma sequência de números de 1 a 5 para o usuário digitar 5 números.
for i in range(1,6):
    # Pedindo ao usuário para digitar um número, utilizando a classe float. 
    numeros = float(input(f'Digite o {i}º número da lista: '))
    # Utilizando o método "append" para adicionar os números digitados pelo usuário ao final da lista "lista_numeros".
    lista_numeros.append(numeros)
# Criando a variável "menor_numero" e igualando ao primeiro elemento da lista "lista_numeros[0]" para iniciar a verificação do menor número.
menor_numero = lista_numeros[0]
# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista e verificar o menor número digitado.
for menor in lista_numeros:
    # Utilizando a estrutura condicional "if" para determinar o menor número.
    if menor < menor_numero:
        # Utilizando o operador de comparação "<" para comparar cada número na lista "lista_numeros" com a variável "menor_numero".
        menor_numero = menor

print(f'O menor número digitado foi: {menor_numero}')
