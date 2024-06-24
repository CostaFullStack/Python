# Questão 10) Dado o dicionário estoque = {'maçã': 10, 'banana': 5, 'laranja': 8, 'uva': 12} peça para o usuário digitar o nome e quantidade de mais 3 frutas, guarde em um novo dicionário e atualize o estoque.

# Criando um dicionário com nome "estoque".
estoque = {
# Utilizando a classe str e adicionando as "chaves" com seus respectivos "valores" utilizando a classe int.
'maçã': 10, 
'banana': 5, 
'laranja': 8, 
'uva': 12
}

# Criando um dicionário vazio para armazenar os nomes das 3 frutas e suas respectivas quantidades.
estoque_novo = {}

# Utilizando a estrutura de repetição FOR para iterar 3 vezes.
for _ in range (3):
    # Pedindo ao usuário para digitar nome e a quantidade da fruta, utilizando a classe "str" e "int". 
    nome_fruta = str(input('Digite o nome da fruta: '))
    qtd_fruta = int(input(f'Digite a quantidade da fruta {nome_fruta}: '))
    # Adicionando os nomes das frutas digitados na variável "nome_fruta" como "chave" no dicionário "estoque" e as quantidades digitadas na variável "qtd_fruta" como "valor".
    estoque[nome_fruta] = qtd_fruta

# Utilizando o método "update" para adicionar as "chaves" e "valores" no novo dicionário "estoque_novo". 
estoque_novo.update(estoque)

# Mostrando na tela o novo dicionário com as novas frutas.
print(f'Estoque com as novas frutas adicionadas: \n{estoque_novo}')