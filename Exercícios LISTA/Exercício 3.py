# Questão 03) Dada a lista notas = [7.5, 8.0, 9.5, 6.0, 8.5], calcule a média das notas e imprima o resultado.

# Criando uma lista com floats de notas.
lista_notas = [7.5, 8.0, 9.5, 6.0, 8.5]
# Iniciando uma variável igual a 0 chamada "soma" para ser realizada a soma das notas percorrendo pela estrutura de repetição FOR.
soma = 0
# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista e realizar a soma das notas.
for nota in lista_notas:
    # Realizando a soma das notas
    soma += nota
# Utilizando a função "len" para retornar o número de itens da lista "lista_notas".
media = soma / len(lista_notas)
# Utilizando a formatação de string para arredodar uma casa decimal. Por exemplo: ".1f" seria uma casa e etc.
print(f'Media das notas: {media:.1f}')
