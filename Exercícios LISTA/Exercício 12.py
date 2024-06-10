# Questão 12) Escreva um programa que solicite ao usuário para inserir palavras até que ele digite "sair". Armazene essas palavras em uma lista e, em seguida, imprima a maior palavra que foi digitada.

# Criando uma lista vazia para armazenar as palavras.
lista_palavras = []
# Iniciando com a estrutura de repetição "while" e utilizando um booleano (True) para se repetir até que o usuário digite a opção de sair.
while True:
    # Pedindo ao usuário para digitar um número, utilizando a classe str. 
    palavras = str(input('Digite uma palavra ou "sair" para encerrar: '))
    # Utilizando a estrutura condicional "if" para verificar se o usuário digitou "sair".
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso a palavra seja igual (==) a sair, o programa é encerrado.
    if palavras.lower().strip() == 'sair':
        # Encerrando o loop.
        break
    # Utilizando o método "append" para adicionar as palavras digitadas pelo usuário ao final da lista "lista_palavras".
    lista_palavras.append(palavras)

# Se a "lista_palavras" for True.
if lista_palavras:
    # Criando a variável "maior_palavra" e igualando ao primeiro elemento da lista "lista_palavras[0]" para iniciar a verificação da maior palavra.
    maior_palavra = lista_palavras[0]
    # Utilizando o operador de associação "in" e a estrutura de repetição FOR para percorrer sobre a lista e verificar a maior palavra digitada.
    for palavra in lista_palavras:
        # Utilizando a estrutura condicional "if" para determinar a maior palavra.
        # Utilizando o operador de comparação ">" para comparar cada palavra na lista "lista_palavras" com a variável "maior_palavra".
        # Utilizando a função len para retornar o número de itens da lista "lista_palavras" e da variável "maior_palavra".
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    print(f'A maior palavra digitada foi: {maior_palavra}')

# Caso o usuário digite apenas "sair".
else:
    print('Nenhuma palavra foi digitada!')