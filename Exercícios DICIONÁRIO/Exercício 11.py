# Questão 11) Dado o dicionário agenda = {'Ana': '555-1234', 'João': '555-5678', 'Maria': '555-4321'}, peça para o usuário escolher o nome de uma pessoa e remover do dicionário a pessoa escolhida.

# Criando um dicionário com nome "agenda".
agenda = {
# Utilizando a classe str e adicionando as "chaves" com seus respectivos "valores" utilizando a classe str.
'Ana': '555-1234', 
'João': '555-5678', 
'Maria': '555-4321'
}

# Criando uma variável chamada "nome_remover" para o usuário digitar o nome de uma pessoa da agenda.
nome_remover = str(input('Digite o nome da pessoa que deseja remover: '))

# Utilizando a estrutura condicional IF e ELSE para determinar se o nome está ou não no dicionário "agenda".
# Utilizando o operador de associação "in" para a condição retornar verdadeira (True).
if nome_remover in agenda:
    # Caso o usuário digite na variável "nome_remover" um nome que esteja no dicionário "agenda", deleta a entrada com "chave" e o "valor" do dicionário.
    del agenda[nome_remover]
    # Mostrando na tela o nome da pessoa removida.
    print(f'Nome "{nome_remover}" removido com sucesso!')

# Caso o usuário digite na variável "nome_remover" um nome que não esteja no dicionário "agenda", uma mensagem de nome não encontrado aparece.
else:
    print('Nome não encontrado na agenda!')

# Mostrando na tela o dicionário com ou não o nome removido.
print(f'Agenda atualizada: {agenda}')
