# Questão 12) Dado o dicionário notas_alunos = {'Ana': [8.0, 7.5, 9.0], 'João': [7.0, 8.5, 9.5], 'Maria': [9.0, 8.0, 8.5]}, mostre na tela o nome e a média do aluno que possui as melhores notas.

dicionario_notas = {
'Ana': [8.0, 7.5, 9.0], 
'João': [7.0, 8.5, 9.5], 
'Maria': [9.0, 8.0, 8.5]
}

nome_melhor = ""
melhor_nota = float('-inf')

for nome,nota in dicionario_notas.items():
    media = sum(nota) / len(nota)
    if media > melhor_nota:
        melhor_nota = media
        nome_melhor = nome

print(f'O aluno com a melhor nota foi: {nome_melhor} com media de: {melhor_nota}')