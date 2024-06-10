# Questão 11) Faça um programa que pede para o usuário digitar um número inteiro e positivo e mostre na tela o fatorial desse número.

# Pedindo ao usuário para digitar um número inteiro e positivo, utilizando a classe int. 
numero = int(input('Digite um número inteiro e positivo para o fatorial: '))
# Utilizando a estrutura condicional IF, e ELSE para determinar se a nota digitada está entre 0 e 10 ou não.   
# Utilizando o operador de comparação "<=" para verificar se a nota digitada é menor ou igual a 0. Caso o usuário digite um número que não atenda a essas "exigências", uma mensagem de erro aparece.
if numero <= 0:
    print('Insira números maiores que 0!')
else:
    # Criando a variável "fatorial"
    fatorial = 1
    # Utilizando a estrutura de repetição FOR para percorrer na variável "numero". Onde o início do range é "1" e o fim do range é "numero +1".
    for i in range(1, numero +1):
            # Calculando o fatorial do número.           
            fatorial *= i

    print(f'O fatorial de {numero} é: {fatorial}')


    