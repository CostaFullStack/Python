# Questão 05) Dada a lista nomes = ['Ana', 'João', 'Maria', 'Pedro'], e a lista idades = [25, 30, 22, 28], crie um dicionário associando cada nome à sua respectiva idade. Imprima o dicionário resultante.

# Criando duas lista com classes str e int.
nomes = ['Ana', 'João', 'Maria', 'Pedro']
idades = [25, 30, 22, 28]

# Criando um dicionário vazio para armazenar os nomes e as idades contidos nas listas "nomes" e "idades".
associando = {}

# Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista "nomes" e realizar a contagem dos nomes das pessoas. Utilizando a função "len" para retornar o número de itens da lista "nomes".
for i in range(len(nomes)):
    # Criando duas variáveis chamadas "nome" e "idade" para associar com as listas "nomes" e "idades" percorrendo pela lista "i".  
    nome = nomes[i]
    idade = idades[i]
    
    # Adicionando a variável "nome" como "chave" no dicionário "associando" e a "idade" como "valor".
    associando[nome] = idade

# Mostrando na tela o dicionário associando os nomes e as idades contidos nas litas "nomes" e "idades".
print(f'Dicionário associando so nomes as suas respectivas idades: \n{associando}')
