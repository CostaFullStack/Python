# Questão 10) Faça um programa que pede 10 números inteiros para o usuário, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

# Iniciando duas variáveis iguais a 0 chamadas "qtd_pares" e "qtd_impares" para realizar a quantidade de números pares e ímpares percorrendo através da estrutura de repetição FOR.
qtd_pares = 0
qtd_impares = 0
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR com range (alcance) de 1 a 11. O fim (número 11) é exclusivo, então será gerada uma sequência de números de 1 a 10 para verificar os números pares e ímpares.
for i in range(1,11):
    # Pedindo ao usuário para digitar um número, utilizando a classe float. 
    numeros = float(input(f'Digite o {i}º número: '))
    # Utilizando a estrutura condicional IF e ELSE para determinar se o número é par ou ímpar.
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 0, o número é par. O operador aritimético "%" retorna o resto da divisão. Então, se a % de 2 for igual (==) a 0, o número é par.
    if numeros %2 == 0:
        # Caso o número seja par, é adicionado mais um na variável "qtd_pares"
        qtd_pares += 1
    # Se a condição acima for falsa (False), ou seja, se a % for diferente (!=) de 0, o número é ímpar.
    else:
        # Caso o número seja ímpar, ou seja, se  a (%2 != 0), é adicionado mais um na variável "qtd_impares"
        qtd_impares += 1

print(f"Quantidade de números pares: {qtd_pares} \nQuantidade de números ímpares: {qtd_impares}")