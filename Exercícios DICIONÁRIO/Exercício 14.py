# Questão 14) Dada a lista de dicionários alunos = [{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]}, {'nome': 'João', 'notas': [7.0, 8.5, 9.5]}, {'nome': 'Maria', 'notas': [9.0, 8.0, 8.5}]}, mostre o nome do aluno que possui a maior média.

# Criando uma lista de dicionário com nome "alunos".
alunos = [
# Utilizando a classe "str" e adicionando as "chaves" com seus respectivos "valores", utilizando uma "lista" contendo notas com a classe "float".
{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]}, 
{'nome': 'João', 'notas': [7.0, 8.5, 9.5]}, 
{'nome': 'Maria', 'notas': [9.0, 8.0, 8.5]}
]

# Iniciando uma variável igual a 0 chamada "media_maior" para realizar a maior média percorrendo pela estrutura de repetição FOR.
media_maior = float("-inf")

# Inciando uma variável igual a "" chamada "nome_maior" para poder realizar o nome do aluno que possui a melhor média percorrendo pela estrutura de repetição FOR.
nome_maior = ""

# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista de dicionário "alunos" e realizar a média dos alunos.
for i in alunos:
    # Criando duas variáveis chamadas "nome" e "notas" para associar com a listas de dicionário "alunos" percorrendo pelo dicionário "i".
    nome = i['nome']
    notas = i['notas'] 
    # Utilizando a função "sum" para retornar a soma dos itens da lista contidas nos "valores" de "notas".
    # Utilizando a função "len" para retornar o número de itens da lista contidas nos "valores" de "notas".
    media = sum(notas) / len(notas)
    # Utilizando a estrutura condicional IF para determinar a maior média.
    # Utilizando o operador de comparação ">" para comparar cada número no dicionário "alunos" com a variável "media_maior".
    if media > media_maior:
        # Igualando a variável "media_maior" a variavel "media" para realizar o aluno com a melhor média, percorrendo sobre o valor "notas".
        media_maior = media
        # Igualando a variável "nome_maior" a chave "nome" para realizar o nome do aluno com a maior média, percorrendo sobre a chave "nome".
        nome_maior = nome

# Mostrando na tela o nome do aluno com as melhores notas.
print(f'Nome do aluno com a maior média: {nome_maior}')