# Questão 02) Escreva uma função chamada media_lista que calcula a média dos valores em uma lista.

lista_valores = [5, 5.6, 7, 8, 9]

def media_lista(lista):
    if not lista:
        return "Lista vazia"
    
    media = sum(lista) / len(lista)
    return media

print(f"Média dos valores presentes na lista: {media_lista(lista_valores):.1f}")



