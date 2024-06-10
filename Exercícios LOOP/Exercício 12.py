# Questão 12) Faça um programa que pede 2 números para o usuário e exibe um menu perguntando qual operação matemática ele quer realizar ou se ele quer encerrar o programa e exiba o resultado na tela a cada escolha do usuário.

# Pedindo ao usuário para digitar dois números, utilizando a classe float. 
primeiro_numero = float(input('Digite um número: '))
segundo_numero = float(input('Digite um número: '))  

# Iniciando com a estrutura de repetição "while" e utilizando um booleano (True) para se repetir até que o usuário digite a opção de sair.
while True:
    try:
        # Criando uma variável menu, utilizando a classe int e pedindo para o usuário digitar uma das opções abaixo.
        menu = int(input("""
Bem vindo ao menu! Por favor, digite umas das opções abaixo:
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
0 - Sair

"""))
        # Utilizando match e case para fazer as operações
        match menu:
            # Se o usuário digitar o número '1'do menu, será feita a soma das variáveis
            case 1:
                print(primeiro_numero + segundo_numero)
            # Se o usuário digitar o número '2'do menu, será feita a subtração das variáveis
            case 2:
                print(primeiro_numero - segundo_numero)
            # Se o usuário digitar o número '3'do menu, será feita a multiplicação das variáveis
            case 3:
                print(primeiro_numero * segundo_numero)
            # Se o usuário digitar o número '4'do menu, será feita a divisão das variáveis
            case 4:
                # Utilizando a estrutura condicional IF e ELSE para verificar se o usuário digitou 0 no segundo número.
                # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso o número seja igual (==) a 0, aparece a mensagem de erro.
                if segundo_numero == 0:
                    print('Erro! Divisão por 0!')
                else:
                    # Caso o número seja maior (>) que 0, a divisão é realizada.
                    print(primeiro_numero / segundo_numero)
            # Se o usuário digitar o número '0' do menu, o loop será encerrado.
            case 0:
                print('Programa encerrado!')
                # Encerrando o loop.
                break
            # Se o usuário digitar um número que não está no menu, aparecerá uma mensagem de erro.
            case _:
                print('Opção inválida. Por favor, digite uma opção válida!')
    # Caso o usuário não digite números, aparecerá uma mensagem de erro.
    except ValueError:
        print('Erro! Digite apenas números!')
        