# Exercício 08) Faça um programa que pede pro usuário escrever um número inteiro entre 1 e 7 e mostre o dia da semana respectivo ao número digitado (1 - domingo, 2 - segunda e etc)

# Pedindo ao usuário para digitar um número para o dia da semana, utilizando a classe int. 
dia_semana = int(input("""
Escolha um número para o respectivo dia da semana:
                       
1 - Domingo
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
7 - Sábado
                       
"""))

# Utilizando a estrutura condicional IF, ELIF e ELSE para determinar os dias da semana.
if dia_semana == 1:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 1, imprime a mensagem informando que é domingo.
    print('Tenha um bom Domingo!')
elif dia_semana == 2:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 2, imprime a mensagem informando que é segunda.
    print('Tenha uma boa Segunda!')
elif dia_semana == 3:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 3, imprime a mensagem informando que é terça.
    print('Tenha uma boa Terça!')
elif dia_semana == 4:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 4, imprime a mensagem informando que é quarta.
    print('Tenha uma boa Quarta!')
elif dia_semana == 5:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 5, imprime a mensagem informando que é quinta.
    print('Tenha uma boa Quinta!')
elif dia_semana == 6:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 6, imprime a mensagem informando que é sexta.
    print('Tenha uma boa Sexta!')
elif dia_semana == 7:
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 7, imprime a mensagem informando que é sábado.
    print('Tenha um bom Sábado!')
else:
    # Caso o usuário informe números diferentes de 1 à 7, imprime a mensagem de opção inválida.
    print('Opção inválida! Por favor, escolha uma opção válida.')

# UTILIZANDO MATCH E CASE
dia_semana= int(input("""             
Escolha um número para o respectivo dia da semana:
                      
1 - Domingo
2 - Segunga
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
7 - Sábado           
                      
"""))

match dia_semana:
# Match é utilizado para comparar um valor com uma série de padrões e executar um bloco de código com base no padrão correspondente
    case 1:
    # Case é utilizado para definir os padrões que o valor de correspondência pode seguir. Cada "case" contém um padrão e um bloco de código associado que será executado se o valor corresponde ao padrão
        # Caso o número seja igual (==) a 1, imprime a mensagem informando que é domingo.
        print('Tenha um bom Domingo!')
    case 2:
        # Caso o número seja igual (==) a 2, imprime a mensagem informando que é segunda.
        print('Tenha uma boa Segunda!')
    case 3:
        # Caso o número seja igual (==) a 3, imprime a mensagem informando que é terça.
        print('Tenha uma boa Terça!')
    case 4:
        # Caso o número seja igual (==) a 4, imprime a mensagem informando que é quarta.
        print('Tenha uma boa Quarta!')
    case 5:
        # Caso o número seja igual (==) a 5, imprime a mensagem informando que é quinta.
        print('Tenha uma boa Quinta!')
    case 6:
        # Caso o número seja igual (==) a 6, imprime a mensagem informando que é sexta.        
        print('Tenha uma boa Sexta!')
    case 7:
        # Caso o número seja igual (==) a 7, imprime a mensagem informando que é sábado.
        print('Tenha um bom Sábado!')
    case _:
        # Caso o usuário informe números diferentes de 1 à 7, imprime a mensagem de opção inválida.
        print('Opção inválida! Por favor, escolha uma opção válida.')




        
