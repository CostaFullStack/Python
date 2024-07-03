# Questão 12) Crie uma função chamada conta_vogais_consoantes que recebe uma string e retorna um dicionário com a contagem de vogais e consoantes presentes na string.

def conta_vogais_consoantes(string):
    soma_vogal = 0
    soma_consoante = 0
    for i in string:
        if i.lower() in "aâáàãeéêèiìíoôõuùúû":
            soma_vogal += 1
        elif i.lower() in "bcçdfghjklmnpqrstvxwyz":
            soma_consoante += 1
    resultado = {"Vogais": soma_vogal, "Consoantes": soma_consoante}
    return resultado

texto = str(input("Digite uma palavra ou um texto: "))
resultado = conta_vogais_consoantes(texto)

print(f"Total de vogais e consoantes na string:\n{resultado}")



