# Questão 09) Escreva uma função chamada conta_pares_impares que recebe uma lista de números e retorna dois valores: a quantidade de números pares e a quantidade de números ímpares na lista.

lista_numeros = []

def conta_pares_impares(lista):
    eh_par = 0
    eh_impar = 0
    for contagem in lista:
        if contagem % 2 == 0:
            eh_par += 1   
        else:
            eh_impar += 1
    return eh_par,eh_impar

for i in range(1,6):
    numero = int(input(f"Digite o {i}º número: "))
    lista_numeros.append(numero)

quantidade_pares = conta_pares_impares(lista_numeros)[0]
quantidade_impares = conta_pares_impares(lista_numeros)[1]

print(f"Quantidade de números pares:{quantidade_pares}\nQuantidade de números ímpares: {quantidade_impares}")
