# Questão 04) Crie um dicionário chamado aluno com as chaves 'nome', 'notas' e 'faltas'. A chave 'notas' deve conter uma lista de três notas. Imprima a média das notas.

# Criando um dicionário com nome "aluno".
aluno = {
# Utilizando a classe "str" e adicionando as "chaves" com seus respectivos "valores" utilizando a classe "str", uma "lista" contendo números com a classe "float".
'nome': 'Matheus Costa Gomes',
'notas': [9.3, 8.5, 7.0],
'faltas': 3
}

# Utilizando a função "sum" para retornar a soma dos itens da lista contidas nos "valores" de "notas".
# Utilizando a função "len" para retornar o número de itens da lista contidas nos "valores" de "notas".
media = sum(aluno['notas']) / len(aluno['notas'])

# Mostrando na tela a média do aluno com a variável "media".
# Utilizando a formatação de string para arredodar uma casa decimal. Por exemplo: ".1f" seria uma casa decimal e etc.
print(f'Média do aluno {aluno["nome"]}: \n{media:.1f}')