# Questão 13) Dada a lista alunos = [{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]}, {'nome': 'João', 'notas': [7.0, 8.5, 9.5]}, {'nome': 'Maria', 'notas': [9.0, 8.0, 8.5}]}, crie uma lista com a média de todos os alunos e mostre na tela em ordem crescente.

dicionario_alunos = [
{'Nome': 'Ana', 'Notas': [8.0, 7.5, 9.0]},
{'Nome': 'João', 'Notas': [7.0, 8.5, 9.5]}, 
{'Nome': 'Maria', 'Notas': [9.0, 8.0, 8.5]}
]

lista_vazia = []

for aluno_da_vez in dicionario_alunos:
    nome = aluno_da_vez['Nome']
    nota = aluno_da_vez['Notas']
    media = sum(nota) / len(nota)
    lista_vazia.append({'nome': nome, 'media': media})

lista_vazia.sort(key=lambda aluno:aluno['media'])

print('Média dos alunos em ordem crescente:')

for aluno in lista_vazia:
    print(f"{aluno['nome']}: {aluno['media']:.1f}")
