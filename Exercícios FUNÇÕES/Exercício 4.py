# Questão 04) Escreva uma função chamada maior_elemento que recebe uma lista de números e retorna o maior deles.

lista_numeros = [1,2,3,4,5,6,17,8,9,10]

def maior_elemento(lista):
    if not lista:
        return "Lista vazia"
        
    maior = max(lista)
    return maior

print(f'O maior número da lista é: {maior_elemento(lista_numeros)}')

    
