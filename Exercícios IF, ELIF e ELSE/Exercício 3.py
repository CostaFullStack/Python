# Questão 03) Faça um programa que pede um número inteiro e positivo para o usuário e mostre na tela se aquele número é par ou ímpar.

# Pedindo ao usuário para digitar um número inteiro e positivo, utilizando a classe int. 
numero_par_impar = int(input('Digite um número inteiro e positivo: '))

# Utilizando a estrutura condicional IF e ELSE para determinar se o número é par ou ímpar.
if numero_par_impar % 2 == 0:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 0, imprime a mensagem informando que o número é par.
    # O operador aritimético "%" retorna o resto da divisão. Então, se a % de 2 for igual (==) a 0, o número é par.  
    print(f'O número {numero_par_impar} é um número par.')
else:
    # Se a condição acima for falsa (False), ou seja, se a % de 2 for diferente (!=) de 0, imprime a mensagem informando que o número é ímpar.
    print(f'O número {numero_par_impar} é um número ímpar.')



