# Questão 13) Desenvolva uma função chamada ordena_produtos que recebe uma lista de dicionários representando produtos (com chaves como 'nome', 'preco', etc.) e retorna a lista ordenada pelo preço em ordem crescente.

produtos = [
{'nome': 'Produto 1', 'preço': 10.0},
{'nome': 'Produto 2', 'preço': 15.0},
{'nome': 'Produto 3', 'preço': 5.0}
]

def ordena_produtos(lista):
    lista_crescente = sorted(lista, key= lambda x: x.get('preço', 0))
    return lista_crescente

resultado = ordena_produtos(produtos)

print("Preço dos produtos em ordem crescente:")
for produto in resultado:
    print(f"""
Produto: {produto['nome']}
Preço: R${produto['preço']}
""")