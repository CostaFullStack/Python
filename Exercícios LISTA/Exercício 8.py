# Questão 08) Crie uma lista chamada números, peça para o usuário inserir 5 números e alimente essa lista, depois mostre a soma de todos os números pares dessa lista.

# Criando uma lista vazia para armazenar os números.
lista_numeros = []
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR com range (alcance) de 1 a 6. O fim (número 6) é exclusivo, então será gerada uma sequência de números de 1 a 5 para o usuário digitar 5 números.
for i in range(1,6):
    # Pedindo ao usuário para digitar um número, utilizando a classe float. 
    numeros = float(input(f'Digite o {i}º número: '))
    # Utilizando o método "append" para adicionar os números digitados pelo usuário ao final da lista "lista_numeros".
    lista_numeros.append(numeros)
# Iniciando uma variável igual a 0 chamada "soma" para ser realizada a soma dos números pares percorrendo pela estrutura de repetição FOR.
soma = 0
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a lista e somar os números pares.
for soma_pares in lista_numeros:
    # Utilizando a estrutura condicional "if" para determinar se o número é par e utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 0, o número é par. O operador aritimético "%" retorna o resto da divisão. Então, se a % de 2 for igual (==) a 0, o número é par.
    if soma_pares % 2 == 0:
        # Realizando a soma dos números pares.
        soma += soma_pares

print(f'A soma dos números pares é de: {soma}')