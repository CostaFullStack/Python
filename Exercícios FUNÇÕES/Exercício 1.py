# Questão 01) Crie uma função chamada soma_numeros que recebe dois números como parâmetros e retorna a soma deles.

def soma_numeros(num1, num2):
    return num1 + num2

numero_um = float(input("Digite um número: "))
numero_dois = float(input("Digite um número: "))

print(f"A soma dos números é: {soma_numeros(num1=numero_um, num2=numero_dois)}")