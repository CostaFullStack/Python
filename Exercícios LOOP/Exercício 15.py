# Faça um programa que pede para o usuário digitar uma senha e cheque se a senha digitada é uma senha forte
# Regras para um senha forte:
# 8 ou mais caracteres
# Pelo menos 1 letra minúscula
# Pelo menos 1 letra maiúscula
# Pelo menos um caractér especial
# Pelo menos 1 número

# Pedindo ao usuário para digitar uma senha, utilizando a classe str. 
senha = str(input('Digite a sua senha: '))
# Utilizando a estruttura condicional "IF" e a função len para verificar se o número é maior (>=) a 8. 
if len(senha) >= 8:
    # Iniciando as variáveis "tem_minuscula", "tem_maiuscula", "tem_especial" e "tem_numero" como False.
    tem_minuscula = False
    tem_maiuscula = False
    tem_numero = False
    tem_especial = False
    # Criando as variáveis "letras", "numeros" e "caracter_especial" para serem verificadas na estrutura de repetição FOR.
    letras = 'abcdefghijklmnopqrstuvxywz'
    numeros = '0123456789'
    caracter_especial = '!@#$%^&*()_+-=[]{|};:"<>,.?/~'

    # Utilizando o operador de associação "in" e a estrutura de repetição "FOR" para percorrer sobre a senha.
    for i in senha:
        # Utilizando a estrutura condicional IF e ELIF para determinar se a senha digitada atende aos requisitos exigidos.
        # Utilizando o operador de associação "in" e a estrutura de repetição "FOR" para percorrer sobre a senha.
        if i in letras:
            # Se estiver presente na variável "letras", a variável "tem_minuscula" se torna True.
            tem_minuscula = True
        elif i in letras.upper():
            # Utilizando a função ".upper()" para verificar se o usuário digitou uma senha maiúscula.
            # Se estiver presente na variável "letras", a variável "tem_maiuscula" se torna True.
            tem_maiuscula = True
        elif i in numeros:
            # Se estiver presente na variável "numeros", a variável "tem_numero" se torna True.
            tem_numero = True
        elif i in caracter_especial:
            # Se estiver presente na variável "caracter_especial", a variável "tem_especial" se torna True.
            tem_especial = True

    # Utilizando a estrutura condicional "IF" e utilizando o operador lógico "and" para a condição retornar verdadeira (True) se as afirmações forem verdadeiras. Aparecendo uma mensagem validando a senha.
    if tem_minuscula and tem_maiuscula and tem_especial and tem_numero:
        print('Senha válida!')
    # Se a senha digitada não atender a todos os requisitos, ou seja, se a condição acima for falsa (False), retorna verdadeiro (True) e imprime a mensagem informando que a senha é inválida.
    else:
        print('Senha inválida!') 
# Caso o usuário digite menos de 8 caracteres, é informado uma mensagem para digitar pelo menos 8 caracteres.
else:
    print('A senha deve conter pelo menos 8 caracteres!')
