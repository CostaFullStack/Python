# Questão 15) Crie uma função que recebe uma senha e verifica se aquela senha é uma senha forte, média ou fraca, requisitos:
# 8 ou mais caracteres
# Pelo menos 1 letra minúscula
# Pelo menos 1 letra maiúscula
# Pelo menos um caractér especial
# Pelo menos 1 número
# Senha forte: Possui todos os requisitos
# Senha média: possui entre 2 e 4 requisitios
# Senha frase: Possui 1 ou menos requisitos

def verifica_senha(senha):
    tamanho = len(senha)
    alfabeto = "abcdefghijklmnopqrstuvxwyz"
    tem_minuscula = 0
    for letra in senha:
        if letra in alfabeto:
            tem_minuscula = 1
            break
    tem_maiuscula = 0
    for letra in senha:
        if letra in alfabeto:
            tem_maiuscula = 1
    tem_especial = 0
    for letra in senha:
        if letra in "!@#$%¨&*()^\~|:;=-_.`´}]{[":
            tem_especial = 1
            break
    tem_numero = 0
    for letra in senha:
        if letra in "0123456789":
            tem_numero = 1
            break
    
    todos_requisitos = tem_minuscula + tem_maiuscula + tem_especial + tem_numero

    if tamanho >= 8 and todos_requisitos == 4:
        return "senha forte"
    elif 2 <= todos_requisitos <= 4:
        return "senha média"
    else:
        return "senha fraca"
    
senha = str(input("Digite a senha: "))
resultado = verifica_senha(senha)

print(f"A senha '{senha}' é uma {resultado}.")
