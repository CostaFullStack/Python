# Questão 11) Escreva uma função chamada menor_maior_elemento que recebe uma lista de números e retorna uma tupla contendo o menor e o maior elemento da lista, respectivamente.

lista_numeros = []

def menor_maior_elemento(lista):
    if not lista:
        return "Lista numeros"
    
    maior = lista[0]
    menor = lista[0]
    
    for num in lista:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num              
    return maior, menor

for num in range(1,6):
    numero = int(input(f"Digite o {num}º número: "))
    lista_numeros.append(numero)

maior_numero = menor_maior_elemento(lista_numeros)[0]
menor_numero = menor_maior_elemento(lista_numeros)[1]

print(f"O maior número da lista é: {maior_numero}\nO menor número da lista é: {menor_numero}")
