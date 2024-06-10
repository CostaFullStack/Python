# Questão 06) Faça um programa que pede para o usuário escrever 3 notas, calcule a média e mostre se ele foi aprovado (acima de 7) ou reprovado.

# Pedindo ao usuário para digitar a nota do aluno, utilizando a classe float. 
primeira_nota = float(input('Digite a 1ª nota: '))
segunda_nota = float(input('Digite a 2ª nota: '))
terceira_nota = float(input('Digite a 3ª nota: '))

# Criando a variável "media" para somar as três notas e dividir por 3
media = (primeira_nota + segunda_nota + terceira_nota) / 3

# Utilizando a estrutura condicional IF e ELSE para determinar se o aluno foi reprovado ou aprovado.
if media >= 7:
    # Utilizando o operador de comparação ">=" para a condição retornar verdadeira (True). Caso a média seja maior ou igual (>=) a 7, imprime a mensagem informando que o aluno foi aprovado.
    # Utilizando a formatção de string para arredodar uma casa decimal. Por exemplo: ".2f" seriam duas casas decimais e etc.

    print(f'O aluno foi aprovado. Média: {media:.1f}')
else:
    # Se a condição acima for falsa (False), retorna verdadeiro (True) e imprime a mensagem informando que o aluno foi reprovado.
    # Utilizando a formatação de string para arredodar uma casa decimal. Por exemplo: ".1f" seria uma casa decimal e etc.
    print(f'O aluno foi reprovado. Média: {media:.1f}')

