# Questão 07) Escreva uma função chamada soma_intervalo que recebe dois números como parâmetros e retorna a soma de todos os números inteiros no intervalo entre eles.

def soma_intervalo(num1, num2):
    soma = 0
    for i in range(num1,num2+1):
        soma += i
    return soma

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero < segundo_numero:
    resultado = soma_intervalo(num1=primeiro_numero, num2=segundo_numero)
    print(f"A soma do intervalo dos números entre {primeiro_numero} e {segundo_numero} é de: {resultado}")
else:
    print("O primeiro número não pode ser maior que o segundo!")