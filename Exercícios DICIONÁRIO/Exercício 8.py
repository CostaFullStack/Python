# Questão 08) Dado o dicionário pessoas = {'João': 25, 'Maria': 30, 'Pedro': 22, 'Ana': 28}, mostre qual nome da pessoa mais velha;

# Criando uma lista de dicionário com nome "pessoas".
pessoas = {
# Utilizando a classe str e adicionando as "chaves" com seus respectivos "valores" utilizando a classe "int".
'João': 25, 
'Maria': 30, 
'Pedro': 22, 
'Ana': 28
}

# Iniciando uma variável igual a 0 chamada "maior" para realizar o maior número, percorrendo pela estrutura de repetição FOR.
idade_mais_velha = 0

# Iniciando uma variável igual a "" chamada "mais_velha" para realizar o nome da pessoa mais velha, percorrendo pela estrutura de repetição FOR.
nome_mais_velha = ""

# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a "chave" e o "valor" do dicionário.
# Utilizando o método ".items()" para percorrer sobre as "chaves" e "valores".
for chave, valor in pessoas.items():
    # Utilizando a estrutura condicional "if" para determinar o nome e a idade da pessoa mais velha.
    # Utilizando o operador de comparação ">" para comparar cada número digitado no "valor" do dicionário "pessoas" com a variável "idade_mais_velha".
    if valor > idade_mais_velha:
        idade_mais_velha = valor
        nome_mais_velha = chave

# Mostrando na tela o nome da pessoa mais velha com a sua respectiva idade.
print(f'O nome da pessoa mais velha é {nome_mais_velha} com {idade_mais_velha} anos.')



