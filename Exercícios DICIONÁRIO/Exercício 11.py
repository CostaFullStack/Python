# Questão 11) Dado o dicionário agenda = {'Ana': '555-1234', 'João': '555-5678', 'Maria': '555-4321'}, peça para o usuário escolher o nome de uma pessoa e remover do dicionário a pessoa escolhida.

dicionario_agenda = {
'Ana': '555-1234', 
'João': '555-5678', 
'Maria': '555-4321'
}

nome_remover = str(input('Digite o nome da pessoa que deseja remover: '))

if nome_remover in dicionario_agenda:
    del dicionario_agenda[nome_remover]
    print(f'Nome removido com sucesso! Lista atualizada: \n{dicionario_agenda}')

else:
    print('Nome não consta na agenda!')


