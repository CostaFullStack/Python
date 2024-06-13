# Questão 03) Dado o dicionário estoque = {'maçã': 10, 'banana': 5, 'laranja': 8, 'uva': 12}, remova a entrada correspondente à 'laranja' e imprima o dicionário atualizado.

dicionario_estoque = {'Maçã': 10, 'Banana': 5, 'Laranja': 8, 'Uva': 12}

del dicionario_estoque['Laranja']

print(f'Dicionário atualizado: \n{dicionario_estoque}')