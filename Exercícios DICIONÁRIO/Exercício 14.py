# Questão 14) Dada a lista de dicionários alunos = [{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]}, {'nome': 'João', 'notas': [7.0, 8.5, 9.5]}, {'nome': 'Maria', 'notas': [9.0, 8.0, 8.5}]}, mostre o nome do aluno que possui a maior média.

dicionario_alunos = [
{'Nome': 'Ana', 'Notas': [8.0, 7.5, 9.0]}, 
{'Nome': 'João', 'Notas': [7.0, 8.5, 9.5]}, 
{'Nome': 'Maria', 'Notas': [9.0, 8.0, 8.5]}
]

nome_maior = ""
maior_media = float("-inf")

for aluno_da_vez in dicionario_alunos:
    nome = aluno_da_vez['Nome']
    nota = aluno_da_vez['Notas']
    media = sum(nota) / len(nota)

    if media > maior_media:
        maior_media = media
        nome_maior = nome

print(f'O nome do aluno com maior média é: {nome}')