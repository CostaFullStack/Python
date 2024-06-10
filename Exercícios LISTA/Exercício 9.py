# Questão 09) Dada a lista [2, 8, 15, 5, 3, 6, 1] remova todos os elementos maiores que 5 e depois mostre a lista atualizada.

# Criando uma lista com floats de números.
lista_numeros = [2, 8, 15, 5, 3, 6, 1]
# Criando uma lista vazia para armazenar os números.
nova_lista = []
# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista e realizar a contagem de numeros menores que 5.
for lista in lista_numeros:
    # Utilizando a estrutura condicional "if" para determinar os números menores que 5 e Utilizando o operador de comparação "<" para comparar cada número na lista "lista_numeros" que são menores (<) que 5 para a condição retorna verdadeira.
    if lista < 5:
        # Utilizando o método "append" na lista vazia "nova_lista" para adicionar a quantidade de numeros que são menores (<) que 5 da lista "lista_numeros".     
        nova_lista.append(lista)

print(f'Lista atualizada: \n{nova_lista}')

