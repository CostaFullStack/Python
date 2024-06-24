# Questão 13) Dada a lista [4, 6, 8, 5, 6, 3, 4, 7, 9, 4, 8] remova todas as duplicatas (números repetido) e mostre a nova lista apenas com itens únicos.

# Criando uma lista com classes floats, alguns repetidos.
lista_numeros = [4, 6, 8, 5, 6, 3, 4, 7, 9, 4, 8]
# Criando uma lista vazia para armazenar os números e deixar os únicos.
nova_lista = []
# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista e realizar a contagem de números únicos.
for lista in lista_numeros:
    # Utilizando a estrutura condicional "if" e o operador de associação "not in" para verificar se  os números repetidos da "lista_numeros" não está em "nova_lista".
    if lista not in nova_lista:
        # Utilizando o método "append" na lista vazia "nova_lista" para adicionar os números únicos da lista "lista_numeros".     
        nova_lista.append(lista)

print(f'Lista com itens únicos: \n{nova_lista}')