# Questão 02) Dado o dicionário notas = {'João': 8.5, 'Maria': 9.0, 'Pedro': 7.5}, adicione a nota 'Ana' com o valor 8.0 e imprima o dicionário atualizado.

# Criando um dicionário com nome "notas"
notas = {
# Utilizando a classe "str" e adicionando as "chaves" com seus respectivos "valores" utilizando a classe "float".
'João': 8.5, 
'Maria': 9.0, 
'Pedro': 7.5
}

# Adicionando o nome "Ana" como "chave" no dicionário "notas" e a nota "8.0" como "valor".
notas['Ana'] = 8.0

# Mostrando na tela o dicionário atualizado com o nome "Ana" e a nota "8.0" adicionada.
print(f'Dicionário atualizado: \n{notas}')