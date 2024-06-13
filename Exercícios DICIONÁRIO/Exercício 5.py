# Questão 05) Dada a lista nomes = ['Ana', 'João', 'Maria', 'Pedro'], e a lista idades = [25, 30, 22, 28], crie um dicionário associando cada nome à sua respectiva idade. Imprima o dicionário resultante.

lista_nomes = ['Ana', 'João', 'Maria', 'Pedro']
lista_idades = [25, 30, 22, 28]

novo_dicionario = {}

for i in range(len(lista_nomes)):
    nomes = lista_nomes[i]
    idades = lista_idades[i]
    novo_dicionario[nomes] = idades


print(f'Dicionário atualizado: \n{novo_dicionario}')




