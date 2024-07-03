# Questão 08) Desenvolva uma função chamada soma_quadrados que recebe dois números inteiros como parâmetros e retorna a soma dos quadrados dos números.

def soma_quadrados(num1,num2):
    soma_quadrado = num1**2 + num2**2
    return soma_quadrado

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
resultado = soma_quadrados(num1=primeiro_numero, num2=segundo_numero)

print(f"A soma dos quadrados dos números é de: {resultado}")
