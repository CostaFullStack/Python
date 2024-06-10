# Questão 14) Faça um programa que pede para o usuário digitar seu salário e calcule o reajuste dele baseado em quanto ele ganha: abaixo de 5.000 reajuste de 15%, entre 5.000 e 10.000 reajuste de 10% acima de
# 10.000 reajuste de 5%.

# Pedindo ao usuário para digitar o salário para ser feito o reajuste, utilizando a classe float. 
salario = float(input('Digite seu salário: '))

# Utilizando a estrutura condicional IF, ELIF e ELSE para determinar a % do reajuste do salário.
if salario < 5000:
    # Utilizando o operador de comparação "<" para a condição retornar verdadeira (True). Caso o salário seja abaixo de 5.000, calcula o reajuste em 15% (0.15).
    salario_reajuste = salario * 0.15
    # Criando a variável "salario_reajuste" para calcular a salário do usuário multiplicando pela porcentagem do reajuste.

elif 5000 <= salario <= 10000:
    # Utilizando o operador de comparação "<=" para a condição retornar verdadeira (True). Caso o salário esteja entre 5000 e 1000, calcula o reajuste em 10% (0.10).
    salario_reajuste = salario * 0.10
    # Criando a variável "salario_reajuste" para calcular a salário do usuário multiplicando pela porcentagem do reajuste.
else:
    # Se a condição acima for falsa (False), retorna verdadeiro (True) e calcula o reajuste acima de 10000 em 5% (0.05).
    salario_reajuste = salario * 0.05    
    # Criando a variável "salario_reajuste" para calcular a salário do usuário multiplicando pela porcentagem do reajuste.

# Criando a variável "novo_salario" para calcular o novo salário com o reajuste.
novo_salario = salario + salario_reajuste

    # Utilizando a formatação de string para arredodar uma casa decimal. Por exemplo: ".1f" seriam uma casa decimal e etc.
print(f'O salário reajustado é de: R${novo_salario:.1f}')