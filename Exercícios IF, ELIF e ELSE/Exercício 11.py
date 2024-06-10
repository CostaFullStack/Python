# Questão 11) Faça um programa que pede para o usuário escrever um número inteiro positivo e mostre na tela se aquele número é ou não divisível por 3 e por 5 ao mesmo tempo.

# Pedindo ao usuário para digitar um número inteiro, utilizando a classe int. 
numero_divisivel = int(input('Digite um número inteiro positivo: '))

# Utilizando a estrutura condicional IF e ELSE para determinar se o número é ou não divísivel por 3 e por 5 ao mesmo tempo.
if numero_divisivel % 3 == 0 and numero_divisivel % 5 == 0:
    # Utilizando o operador de comparação "==" e o operador lógico "and" para ambas as condições retornarem verdadeiras (True). 
    # O operador aritimético "%" retorna o resto da divisão. Então, se a % de 3 e de 5 for igual (==) a 0, imprime a mensagem informando que o número é divísvel por 3 e por 5.  
    print(f'O número {numero_divisivel} é divisível por 3 e por 5.')
else:
    # Se a condição acima for falsa (False), ou seja, se a % for diferente (!=) de 0, imprime a mensagem informando que o número não é divísvel por 3 e por 5.
    print(f'O número {numero_divisivel} não é diivísvel por 3 e por 5.')