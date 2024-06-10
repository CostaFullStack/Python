# Questão 12) Dada a senha 123456Ab. faça um programa que pede para o usuário inserir uma senha, se ele acertar a senha mencionada acima, mostre uma mensagem de acesso liberado, caso contrario, acesso negado.

# Criando a variável "senha" para o usuário poder confirmar
senha = '123456Ab'
# Pedindo ao usuário para confirmar a senha acima, utilizando a classe str. 
senha_confirma = str(input('Digite a senha: '))

# Utilizando a estrutura condicional IF e ELSE para determinar se a senha digitada é ou não correta.
if senha_confirma == senha:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso a senha confirmada seja igual a senha, imprime a mensagem informando que o acesso foi liberado.
    print('Acesso liberado.')
else:
    # Se a condição acima for falsa (False), retorna verdadeiro (True) e imprime a mensagem informando que o acesso foi negado.
    print('Acesso negado.')
