# Questão 05) Crie uma lista chamada números, peça para o usuário inserir 5 números e alimente essa lista, depois mostre o maior número dessa lista.

# Criando uma lista vazia para armazenar os números.
lista_numeros = []
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR com range (alcance) de 1 a 6. O fim (número 6) é exclusivo, então será gerada uma sequência de números de 1 a 5 para o usuário digitar 5 números.
for i in range(1,6):
    # Pedindo ao usuário para digitar um número, utilizando a classe float. 
    numeros = float(input(f'Digite o {i}º número: '))
    # Utilizando o método "append" para adicionar os números digitados pelo usuário ao final da lista "lista_numeros".
    lista_numeros.append(numeros)

# Criando a variável "maior_numero" e igualando ao primeiro elemento da lista "lista_numeros" para iniciar a verificação do maior número.
maior_numero = lista_numeros[0]
# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista e verificar o maior número digitado.
for maior in lista_numeros:
    # Utilizando a estrutura condicional "if" para determinar o maior número.
    # Utilizando o operador de comparação ">" para comparar cada número na lista "lista_numeros" com a variável "maior_numero".
    if maior > maior_numero:
        maior_numero = maior

print(f'O maior número digitado foi: {maior_numero}')