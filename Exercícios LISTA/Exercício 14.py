# Questão 14) Dadas as listas [5, 1, 9, 3, 4, 7] e [1, 8, 2, 7, 5, 0] faça uma varredura e crie uma nova lista contendo apenas os números que estejam contidos nas duas listas.

# Criando duas listas com classes ints.
lista_numeros1 = [5, 1, 9, 3, 4, 7]
lista_numeros2 = [1, 8, 2, 7, 5, 0] 

# Criando uma lista vazia para armazenar os números e deixar os apenas os contidos nas duas listas.
nova_lista = []

# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista "lista_numeros1" e realizar a contagem de números contidos nas duas listas.
for lista in lista_numeros1:
    # Utilizando a estrutura condicional "if" e o operador de associação "in" para verificar se os números contidos da "lista_numeros1" estão em "lista_numeros2".
    if lista in lista_numeros2:
        # Utilizando o método "append" na lista vazia "nova_lista" para adicionar os números contidos na lista "lista_numeros1" e "lista_numeros2".     
        nova_lista.append(lista)

print(f'Lista com números contidos nas duas listas: \n{nova_lista}')