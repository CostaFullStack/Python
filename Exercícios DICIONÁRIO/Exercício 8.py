# Questão 08) Dado o dicionário pessoas = {'João': 25, 'Maria': 30, 'Pedro': 22, 'Ana': 28}, mostre qual nome da pessoa mais velha;

dicionario_pessoas = {'João': 25, 'Maria': 30, 'Pedro': 22, 'Ana': 28}

nome_mais_velho = ""
idade_mais_velho = float('-inf')

for nome,idade in dicionario_pessoas.items():
    if idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome

print(f'O nome da pessoa mais velha é {nome_mais_velho} com {idade_mais_velho} anos.')
