# Questão 03) Faça um programa que pede para o usuário digitar 8 notas e no final calcula a média dessas notas.

# Iniciando uma variável igual a 0 chamada "soma" para ser realizada a soma das notas através da estrutura de repetição FOR.
soma = 0
# Utilizando a estrutura de repetição FOR com range (alcance) de 1 a 11. O fim (número 11) é exclusivo, então será gerada uma sequência de números de 1 a 10.
for i in range(1,9):
    # Pedindo ao usuário para digitar os números, utilizando a classe float. 
    notas = float(input(f"Digite a {i}ª nota: "))
    # Fazendo a soma dos números 
    soma += notas
# Fazendo a média das notas
media = soma / 8
# O método ".1f" arredonda uma casa após a vírgula. ".2f" seriam duas casas e etc.
print(f"A média das notas é de: {media:.1f}")