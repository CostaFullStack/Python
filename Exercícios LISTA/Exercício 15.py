# Questão 15) Dada a lista produtos =[('Mouse', 25.99), ('Teclado',59.99), ('Mousepad', 15.99), ("Monitor", 600.00),("Fone de Ouvido", 110.50)], ordene a lista com base no segundo elemento de cada tupla (o preço) em ordem crescente.

# Criando uma lista com tuplas contendo ints e strs.
lista_produtos =[('Mouse', 25.99), ('Teclado',59.99), ('Mousepad', 15.99), ("Monitor", 600.00),("Fone de Ouvido", 110.50)]
# Criando uma lista vazia para armazenar apenas os números contidos na lista.
nova_lista = []
# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista "lista_produtos".
for lista in lista_produtos:
        # Utilizando o método "append" na lista vazia "nova_lista" para adicionar os números (que são o segundo elemento) contidos na lista "lista_produtos".     
        nova_lista.append(lista[1])

# Utilizando o método sort para ordenar a lista em ordem crescente.
nova_lista.sort()

print(f'Preço da lista em ordem crescente:')
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a lista e imprimir os números em ordem crescente de forma separada.
for lista in nova_lista:
    print(lista)