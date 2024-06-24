# Questão 01) Crie um dicionário chamado pessoa com as chaves 'nome', 'idade', ‘altura’ e 'cidade'. Peça para o usuário preencher os dados e imprima o dicionário.

# Criando um dicionário com nome "pessoa".
pessoa = {
# Pedindo ao usuário para preencher os dados, utilizando as classes "str", "int" e "float".
'nome': str(input('Digite o seu nome: ')),
'idade': int(input('Digite a sua idade: ')),
'altura': float(input('Digite a sua altura: ')),
'cidade': str(input('Digite a sua cidade: '))
}

# Mostrando na tela os dados da pessoa chamando o nome do dicionário e utilizando suas respectivas "chaves" e "valores". 
print(f"""
Dados da pessoa:
Nome: {pessoa['nome']}
Idade: {pessoa['idade']} anos
Altura: {pessoa['altura']} M
Cidade: {pessoa['cidade']}
""")