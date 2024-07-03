# Questão 10) Crie uma função chamada celsius_para_fahrenheit que converte uma temperatura em graus Celsius para Fahrenheit. A fórmula de conversão é: F = (C *9/5) + 32.

def celsius_para_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

temperatura = float(input("Digite a temperatura em Celsius: "))
resultado = celsius_para_fahrenheit(temperatura)

print(f"A temperatura convertida de Celsius para Fahrenheit é de: {resultado:.2f}ºF")

