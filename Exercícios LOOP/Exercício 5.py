# Questão 05) Faça um programa que pede para o usuário digitar uma frase e conte quantas letras A existem na frase e mostre na tela a quantidade encontrada.

# Pedindo ao usuário para digitar uma frase, utilizando a classe str. 
frase = str(input('Digite uma frase: '))
# Iniciando uma variável igual a 0 chamada "letras_a" para ser realizada a soma das letras "A"'s percorrendo pela estrutura de repetição FOR.
letras_a = 0
# Utilizando o operador de associação "in" a estrutura de repetição FOR para percorrer sobre a frase e contar a(s) letra(s) "a".
# Utilizando a função ".lower()" para converter a variável "frase" para minúscula e a função ".strip()" para remover espaços extras.
for i in frase.lower().strip():
    # Utilizando a estrutura condicional "if" para determinar se possui letra "A" na frase.
    # Utilizando o operador de associação "in" para a condição retornar verdadeira (True). Caso a letra seja encontrada, a mesma é adicionada à soma.
    if i in "aáãâà":
        # Fazendo a soma das letras
        # Utilizando a função len para retornar o número de itens na frase.
        letras_a += len(i)

print(f'A frase "{frase}" tem {letras_a} letra(s) "A".')


