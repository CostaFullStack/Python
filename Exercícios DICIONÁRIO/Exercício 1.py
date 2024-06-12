# Questão 01) Crie um dicionário chamado pessoa com as chaves 'nome', 'idade', ‘altura’ e 'cidade'. Peça para o usuário preencher os dados e imprima o dicionário.

dicionario_pessoa = {
'Nome': str(input('Digite o nome da pessoa: ')),
'Idade': int(input('Digite a idade: ')),
'Altura': float(input('Digite a altura: ')),
'Cidade': str(input('Digite a cidade: '))
}

print(f"""
Dados da pessoa:
Nome: {dicionario_pessoa['Nome']}
Idade: {dicionario_pessoa['Idade']} anos
Altura: {dicionario_pessoa['Altura']} CM
Cidade: {dicionario_pessoa['Cidade']}
""")
