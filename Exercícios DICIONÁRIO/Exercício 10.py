# Questão 10) Dado o dicionário estoque = {'maçã': 10, 'banana': 5, 'laranja': 8, 'uva': 12} peça para o usuário digitar o nome e quantidade de mais 3 frutras, guarde em um novo dicionário e atualize o estoque.

dicionario_estoque = {
'Maçã': 10, 
'Banana': 5, 
'Laranja': 8, 
'Uva': 12
}

novo_dicionario = {}

for _ in range(3):
    nome_fruta = str(input(f'Digite o nome da {_+1}ª fruta: '))
    qtd_fruta = int(input('Digite a quantidade: '))
    novo_dicionario[nome_fruta] = qtd_fruta

dicionario_estoque.update(novo_dicionario)

print(f"Estoque atualizado: \n{dicionario_estoque}")