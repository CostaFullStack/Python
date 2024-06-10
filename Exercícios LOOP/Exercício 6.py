# Questão 06) Faça um programa que pede para o usuário digitar uma frase e mostre na tela quantas consoantes existem naquela frase.

# Pedindo ao usuário para digitar uma frase, utilizando a classe str. 
frase = str(input('Digite uma frase: '))
# Iniciando uma variável igual a 0 chamada "soma_consoantes" para ser realizada a soma das letras "A"'s percorrendo pela estrutura de repetição FOR.
soma_consoantes = 0
# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer na frase e contar as consoantes.
# Utilizando a função .lower() para converter a variável "frase" para minúscula e a função .strip() para remover espaços extras.
for i in frase.lower().strip():
    # Utilizando a estrutura condicional "if" para determinar se possui consoantes na frase.
    # Utilizando o operador de associação "in" para a condição retornar verdadeira (True). Caso a letra seja encontrada, a mesma é adicionada à soma.
    if i in "bcdfghjklmnpqrstyvxwz":
        # Fazendo a soma das consoantes
        # Utilizando a função len para retornar o número de itens na frase.
        soma_consoantes += len(i)

print(f'A frase "{frase}" tem {soma_consoantes} consoantes.')
