# Questão 02) Faça um programa que pede para o usuário digitar 10 números e mostre na tela a soma de todos os números digitados.

# Iniciando uma variável igual a 0 chamada "soma" para ser realizada a soma dos números através da estrutura de repetição FOR.
soma = 0
# Utilizando o operador de associação "in" e a estrutura de repetição FOR com range (alcance) de 1 a 11. O fim (número 11) é exclusivo, então será gerada uma sequência de números de 1 a 10.
for i in range(1,11):
    # Pedindo ao usuário para digitar os números, utilizando a classe float. 
    numeros = float(input(f'Digite o {i}º número: '))
    # Fazendo a soma dos números 
    soma += numeros
# Utilizando o print fora da estrutura de repetição FOR para ser mostrada a soma final de todos os números uma única vez.
print(f"A soma dos números digitados foi de: {soma}")
