# Questão 07) Dada a lista de dicionários alunos = [{'nome': 'Ana', 'nota': 8.5}, {'nome': 'João', 'nota': 7.0}, {'nome': 'Maria', 'nota': 9.5}], ordene a lista com base nas notas em ordem decrescente.

lista_alunos = [
{'Nome': 'Ana', 'Nota': 8.5}, 
{'Nome': 'João', 'Nota': 7.0}, 
{'Nome': 'Maria', 'Nota': 9.5}
]

lista_alunos.sort(key=lambda nota:nota['Nota'], reverse=True)

print('Lista de dicionários em ordem decrescente:')
for aluno_da_vez in lista_alunos:
    print(aluno_da_vez)