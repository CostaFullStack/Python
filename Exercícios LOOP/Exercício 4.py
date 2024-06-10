# Questão 04) Faça um programa que mostra a soma de todos os números entre o 1 e o 500.

# Iniciando uma variável igual a 0 chamada "soma" para ser realizada a soma dos números através da estrutura de repetição FOR.
soma = 0
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR com range (alcance) de 1 a 501. O fim (número 501) é exclusivo, então será gerada uma sequência de números de 1 a 10.
for i in range (1,501):
    # Fazendo a soma dos números 
    soma += i
# Utilizando o print fora da estrutura de repetição FOR para ser mostrada a soma final de todos os números uma única vez.
print(f"A soma dos números entre 1 a 500 é de: {soma}")