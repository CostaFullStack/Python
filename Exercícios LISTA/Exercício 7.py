# Questão 07) Dada a lista palavras = ['python', 'java', 'c++', 'javascript'], crie uma nova lista contendo o número de caracteres de cada palavra. Imprima a lista resultante item por item.

# Criando uma lista com classes strings de linguagens de programação.
lista_palavras = ['Python', 'Java', 'C++', 'Javascript']
# Criando uma lista vazia para armazenar os números de caracteres de cada palavra.
nova_lista = []
# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista e realizar a contagem de caracteres.
for lista in lista_palavras:
    # Utilizando o método "append" na lista vazia "nova_lista" para adicionar a quantidade de caractéres que contém nas strings da lista "lista_palavras".
    # Utilizando a função len para retornar o número de itens da lista "lista_palavras".
    nova_lista.append(len(lista))
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a lista e imprimir a quantidade de caracteres de cada palavra.
for lista in nova_lista:
    print(lista)