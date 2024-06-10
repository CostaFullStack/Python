# Questão 9) Faça um programa que pergunte qual ano o usuário nasceu e mostre na tela se ele é ou não maior de idade

# Pedindo ao usuário para digitar ano em que nasceu, utilizando a classe int. 
ano_nascimento = int(input('Digite o ano que você nasceu: '))

# Criando a variável "idade" para calcular a idade do usuário subtraindo o ano de nascimento do ano atual (2024)
idade = 2024 - ano_nascimento

# Utilizando a estrutura condicional IF e ELSE para determinar se o usuário é menor ou maior de idade.
if idade >= 18:
    # Utilizando o operador de comparação ">=" para a condição retornar verdadeira (True). Caso a idade seja maior ou igual (>=) a 18, imprime a mensagem informando que é maior de idade.
    print(f'Você tem {idade} anos. Você é maior de idade.')
else:
    # Se a condição acima for falsa (False), retorna verdadeiro (True) e imprime a mensagem informando que o aluno é menor de idade.
    print(f'Você tem {idade} anos. Você é menor de idade.')