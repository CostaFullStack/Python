# Questão 11) Dada a lista pontuacoes = [98, 72, 86, 94, 88], imprima na tela essa mesma lista em ordem descrescente.

# Criando uma lista com classes ints.
lista_pontuacoes = [98, 72, 86, 94, 88]

# Utilizando o método sort para ordenar a lista e utilizando o "reverse=True" para deixar em ordem decrescente
lista_pontuacoes.sort(reverse=True)

print(f'Lista em ordem descrescente: \n{lista_pontuacoes}')