# Questão 09) Faça um programa que pede para o usuário uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# Iniciando com a estrutura de repetição "while" e utilizando um booleano (True) para se repetir até que o usuário digite uma nota válida.
while True:
    # Pedindo ao usuário para digitar uma nota, utilizando a classe float. 
    nota = float(input('Digite uma nota entre 0 e 10: '))
    # Utilizando a estrutura condicional IF e ELSE para determinar se a nota digitada está ou não entre 0 e 10   
    # Utilizando o operador de comparação ">" para verificar se a nota digitada é maior que 10 e o operador de comparação "<" para verificar se a nota digitada é menor que 0. Caso o usuário digite uma nota que não atenda a essas "exigências", uma mensagem de erro aparece, se repetindo até que o usuário digite uma nota entre 0 e 10.
    if nota > 10 or nota < 0:
        print('Nota inválida! Por favor, informe uma nota entre 0 e 10!')

    else:
        # Caso o usuário digite uma nota entre 0 e 10 (nota <= 10 and nota >= 0), uma mensagem de nota aparece. 
        print(f'Nota digitada:\n{nota}')
        # Encerrando o loop.
        break