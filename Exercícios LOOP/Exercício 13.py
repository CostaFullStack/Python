# Questão 13) Faça um programa que pede para o usuário digitar um número inteiro e positivo e mostre na tela se ele é ou não um número primo.

# Pedindo ao usuário para digitar um número inteiro e positivo, utilizando a classe int. 
numero = int(input('Digite um número inteiro e positivo: '))

# Utilizando a estruttura condicional IF para verificar se o número é maior (>) que 1. 
if numero > 1:
    # Criando a variável "divisor" igual a 0 para realizar a quantidade de divisores percorrendo através da estrutura de repetição FOR.
    divisor = 0
    # Criando uma variável "raiz_quadrada" para a raiz quadrada e utilizar na estrutura de repetição FOR.
    raiz_quadrada = int(numero ** 0.5)
    # Utilizando a estrutura de repetição FOR. Onde o início do range é "2" e o fim do range é a variável "raiz_quadrada" +1.
    for i in range(2, raiz_quadrada + 1):
        # Utilizadno a estrutura condicional IF e o operador de comparação "==" para a condição retornar verdadeira (True). Caso a variável "numero" com % de "i" seja igual (==) a 0, o número é primo. O operador aritimético "%" retorna o resto da divisão. Então, se a variável "numero" % de i for igual (==) a 0, o número é primo.
        if numero % i == 0:
            divisor += 1
            # Encerrando o loop.
            break
    # Utilizando a estrutura condicional IF e ELSE para verificar se o número é ou não primo.
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso a variável "divisor" seja igual (==) a 0, aparece a mensagem informando que é primo.      
    if divisor == 0:
        print(f'O número {numero} é um número primo!')
    else:
        # Caso a variável "divisor" seja diferente (!=) de 0, aparece a mensagem informando que não é primo.
        print(f'O número {numero} não é um número primo!')
# Caso o usuário digite um número menor ou igual (<=) a 0.
else:
    print('Número inválido! Digite um número inteiro e positivo maior que 1!')