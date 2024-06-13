# Questão 04) Crie um dicionário chamado aluno com as chaves 'nome', 'notas' e 'faltas'. A chave 'notas' deve conter uma lista de três notas. Imprima a média das notas.

dicionario_aluno = {
'Nome': str(input('Digite o nome do aluno: ')),
'Notas': [8,9,10], 
'Faltas': int(input('Digite a quantidade de faltas: '))
}

media = sum(dicionario_aluno['Notas']) / len(dicionario_aluno['Notas'])

print(f'A média do aluno {dicionario_aluno["Nome"]} é de: {media:.1f}')