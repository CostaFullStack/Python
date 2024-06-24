# Questão 09) Dada a lista de dicionários pessoas = [{'nome': 'Ana', 'idade': 16}, {'nome': 'João', 'idade': 30}, {'nome': 'Maria', 'idade': 17}], crie uma lista com o nome das pessoas que possuem menos que 18 anos.

# Criando uma lista de dicionário com nome "pessoas".
pessoas = [
# Utilizando a classe str e adicionando as "chaves" com seus respectivos "valores" utilizando a classe "int".
{'nome': 'Ana', 'idade': 16}, 
{'nome': 'João', 'idade': 30}, 
{'nome': 'Maria', 'idade': 17}
]

# Criando uma lista vazia para armazenar os nomes das pessoas com menos de 18 anos.
pessoas_menor = []

# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista e realizar a contagem dos nomes das pessoas que possuem menos de 18 anos.
for i in pessoas:
    # Utilizando a estrutura condicional "if" para determinar os nomes que são menores de 18 anos.
    # Utilizando o operador de comparação "<" para comparar com os "valor" da lista de dicionário "pessoas" das chaves "idade".
    if i['idade'] < 18:
        # Utilizando o método "append" para adicionar os números menores de 18 ao final da lista "pessoas_menor".
        # Percorrendo sobre a "chave" "nome" para adicionar os nomes.
        pessoas_menor.append(i['nome'])

# Mostrando na tela a lista das pessoas que tem menos de 18 anos.
print(f'Lista de pessoas com menos de 18 anos: \n{pessoas_menor}')