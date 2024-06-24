# Questão 03) Dado o dicionário estoque = {'maçã': 10, 'banana': 5, 'laranja': 8, 'uva': 12}, remova a entrada correspondente à 'laranja' e imprima o dicionário atualizado.

# Criando um dicionário com nome "estoque" 
estoque = {
# Utilizando a classe "str" e adicionando as "chaves" com seus respectivos "valores" utilizando a classe "int".
'maçã': 10, 
'banana': 5, 
'laranja': 8, 
'uva': 12
}

# Deletando a entrada com "chave" igual a "laranja" do dicionário "estoque".
del estoque['laranja']

# Mostrando na tela o dicionário atualizado com a chave "laranja" removida.
print(f'Dicionário atualizado: \n{estoque}')