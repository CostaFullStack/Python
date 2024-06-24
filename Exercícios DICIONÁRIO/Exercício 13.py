# Questão 13) Dada a lista alunos = [{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]}, {'nome': 'João', 'notas': [7.0, 8.5, 9.5]}, {'nome': 'Maria', 'notas': [9.0, 8.0, 8.5}]}, crie uma lista com a média de todos os alunos e mostre na tela em ordem crescente.

# Criando uma lista de dicionário com nome "alunos".c
alunos = [
# Utilizando a classe "str" e adicionando as "chaves" com seus respectivos "valores", utilizando uma "lista" contendo notas com a classe "float".
{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]}, 
{'nome': 'João', 'notas': [7.0, 8.5, 9.5]}, 
{'nome': 'Maria', 'notas': [9.0, 8.0, 8.5]}
]

# Criando uma lista vazia para armazenar as médias.
lista_media = []

# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista de dicionário "alunos" e realizar a média dos alunos.
for i in alunos:
    # Criando duas variáveis chamadas "nome" e "notas" para associar com a listas de dicionário "alunos" percorrendo pelo dicionário "i".
    nome = i['nome']
    notas = i['notas']
    # Utilizando a função "sum" para retornar a soma dos itens da lista contidas nos "valores" de "notas".
    # Utilizando a função "len" para retornar o número de itens da lista contidas nos "valores" de "notas".
    media = sum(notas) / len(notas)
    # Utilizando o método "append" para adicionar o nome e a média ao final da lista "lista_media".
    # Percorrendo sobre a "chave" "nome" e o valor "media" para adicionar os nomes e as médias dos respectivos alunos.
    lista_media.append({'nome': nome, 'media': media})

# Utilizando o método "sort" para ordenar a lista e utilizando para deixar em ordem crescente.
lista_media.sort(key=lambda aluno: aluno['media'])

print('Média dos alunos em ordem crescente:')
# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a lista e imprimir o nome e a média de cada aluno.
for aluno in lista_media:
    # Mostrando na tela os dados dos alunos chamando o nome da lista e utilizando suas respectivas "chaves" e "valores". 
    print(f"""
Aluno(a): {aluno['nome']}
Média: {aluno['media']:.1f}
""")




