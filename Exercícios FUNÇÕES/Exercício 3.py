# Questão 03) Implemente uma função chamada eh_par que recebe um número como argumento e retorna True se o número for par e False caso contrário.

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número: "))
resultado = eh_par(numero)

if resultado:
    print(f"O número {numero} é par.")

else:
    print(f"O número {numero} é ímpar.")