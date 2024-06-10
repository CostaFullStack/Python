# Questão 13) Faça um programa que pergunte o nome do usuário e que horas são e mostre na tela um cumprimento por exemplo “Bom dia fulano” ou “Boa noite fulano” ou “Boa tarde fulano”

# Pedindo ao usuário para digitar o nome, utilizando a classe str. 
nome = str(input('Digite seu nome: '))
# Pedindo ao usuário para informar as horas, utilizando a classe int. 
hora_atual = int(input('Informe as horas (NÃO INCLUA MINUTOS NEM SEGUNDOS): '))

# Utilizando a estrutura condicional IF e ELSE para determinar as horas.
if 5 <= hora_atual < 12:
    # Utilizando os operadores de comparação "<=" e "<" para a condição retornar verdadeira (True). Caso esteja entre os horários de 5 às 11, imprime a mensagem de bom dia.
    print(f'Bom dia, {nome}.')
elif 12 <= hora_atual < 18:
    # Utilizando os operadores de comparação "<=" e "<" para a condição retornar verdadeir (True). Caso esteja entre os horários de 12 às 17, imprime a mensagem de boa tarde.
    print(f'Boa tarde, {nome}.')
else:
    # Se as condições acima forem falsas (False), imprime a mensagem de boa noite.
    print(f'Boa noite, {nome}.')
