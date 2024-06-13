# Questão 09) Dada a lista de dicionários pessoas = [{'nome': 'Ana', 'idade': 16}, {'nome': 'João', 'idade': 30}, {'nome': 'Maria', 'idade': 17}], crie uma lista com o nome das pessoas que possuem menos que 18 anos.

lista_pessoas = [{'Nome': 'Ana', 'Idade': 16}, {'Nome': 'João', 'Idade': 30}, {'Nome': 'Maria', 'Idade': 17}]

nova_lista = []

for menor in lista_pessoas:
    if menor['Idade'] < 18:
        nova_lista.append(menor['Nome'])

print(f'Lista atualizada com menores de 18 anos: \n{nova_lista}')