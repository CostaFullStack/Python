# Questão 07) Dada a lista de dicionários alunos = [{'nome': 'Ana', 'nota': 8.5}, {'nome': 'João', 'nota': 7.0}, {'nome': 'Maria', 'nota': 9.5}], ordene a lista com base nas notas em ordem decrescente.

# Criando uma lista de dicionário com nome "alunos".
alunos =  [
# Utilizando a classe "str" e adicionando as "chaves" com seus respectivos "valores" utilizando a classe "float".
{'nome': 'Ana', 'nota': 8.5}, 
{'nome': 'João', 'nota': 7.0}, 
{'nome': 'Maria', 'nota': 9.5}
]

# Utilizando o método "sort" para ordenar a lista de dicionários e utilizando o "reverse=True" para deixar em ordem decrescente.
alunos.sort(key=lambda aluno:aluno['nota'], reverse=True)

print('Notas em ordem decrescente:')

# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a lista de dicionários. Imprimindo no final a lista de dicionários em ordem decrescente.
for i in alunos:
    print(i)