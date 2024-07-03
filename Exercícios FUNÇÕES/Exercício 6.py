# Questão 06) Crie uma função chamada conta_caracteres que recebe uma string e retorna a quantidade de caracteres que não sejam espaços vazios.

def conta_caracteres(string):
    soma = 0
    for i in string:
        if i != " ":
            soma += 1          
    return soma

texto = str(input("Digite um texto: "))
resultado = conta_caracteres(texto)

print(f"O texto {texto} possui {resultado} caracteres.")
