# Questão 12) Dado o dicionário notas_alunos = {'Ana': [8.0, 7.5, 9.0], 'João': [7.0, 8.5, 9.5], 'Maria': [9.0, 8.0, 8.5]}, mostre na tela o nome e a média do aluno que possui as melhores notas.

# Criando um dicionário com nome "notas_alunos".
notas_alunos = {
# Utilizando a classe "str" e adicionando as "chaves" com seus respectivos "valores", utilizando uma "lista" contendo notas com a classe "float".
'Ana': [8.0, 7.5, 9.0], 
'João': [7.0, 8.5, 9.5], 
'Maria': [9.0, 8.0, 8.5]
}

# Iniciando uma variável igual a 0 chamada "melhor_nota" para poder realizar a média da melhor nota percorrendo pela estrutura de repetição FOR.
melhor_nota = 0

# Inciando uma variável igual a "" chamada "nome_maior" para poder realizar o nome do aluno que possui a melhor média percorrendo pela estrutura de repetição FOR.
nome_maior = ""

# Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a "chave" e o "valor" do dicionário.
# Utilizando o método ".items()" para percorrer sobre as "chaves" e "valores".
for nome, nota in notas_alunos.items():
    # Utilizando a função "sum" para retornar a soma dos itens da lista contidas nos "valores" de "notas".
    # Utilizando a função "len" para retornar o número de itens da lista contidas nos "valores" de "notas".
    media = sum(nota) / len(nota)
    # Utilizando a estrutura condicional IF para determinar a maior média.
    # Utilizando o operador de comparação ">" para comparar cada número no dicionário "notas_alunos" com a variável "melhor_nota".
    if media > nota_maior:
        # Igualando a variável "nota_maior" a chave "nota" para realizar o aluno com a melhor média, percorrendo sobre o valor "nota".
        nota_maior = media
        # Igualando a variável "nome_maior" a chave "nome" para realizar o nome do aluno com a maior média, percorrendo sobre a chave "nome".
        nome_maior = nome

# Mostrando na tela o nome e a média do aluno com as melhores notas.
print(f'O nome do aluno com a maior média é {nome_maior} com a média de: {nota_maior}')