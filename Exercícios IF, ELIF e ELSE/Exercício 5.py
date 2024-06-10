# Questão 05) Faça um programa que pede para o usuário digitar uma letra (M ou F) e mostra uma mensagem respectiva M - Masculino, F - Feminino ou Sexo inválido

# Pedindo ao usuário para digitar uma letra, utilizando a classe str. 
# Utilizando o método .upper() para converter a variável "informe_sexo" para maiúscula e o método .strip() para remover espaços extras.
informe_sexo = str(input("""
Digite o sexo:
                         
M - Masculino
F - Feminino
                         
""")).upper().strip()

# Utilizando a estrutura condicional IF, ELIF e ELSE para determinar se o sexo é Feminino, Masculino ou Sexo inválido.
if informe_sexo == "F":
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso a letra seja encontrada, imprime a mensagem informando que o sexo é feminino.
    print(f'O sexo informado é feminino.')
elif informe_sexo == "M":
    # Se a condição acima for falsa (False), utiliza o operador de comparação "==" para a condição retornar verdadeira (True). Caso a letra seja encontrada, imprime a mensagem informando que o sexo é masculino.
    print(f'O sexo informado é masculino.')
else:
    # Se as condições acima forem falsas (False), retorna verdadeiro (True) e imprime a mensagem informando que o sexo é inválido.
    print('Sexo inválido.')
