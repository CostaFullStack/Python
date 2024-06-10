# Questão 15) Os teclados custam R$ 30 cada se forem compradas menos do que uma dúzia, e R$ 25 se forem compradas pelo menos doze. Escreva um programa que leia o número de teclados compradas, 
# calcule e escreva o valor total da compra.

# Pedindo ao usuário para digitar a quantidade de teclados para ser realizado o valor total da compra, utilizando a classe int. 
teclado_qtd = int(input('Digite a quantidade de teclados comprados: '))

# Utilizando a estrutura condicional IF e ELSE para determinar o preço dos teclados.
if teclado_qtd >= 12:
    # Utilizando o operador de comparação ">=" para a condição retornar verdadeira (True). Caso seja comprado 12 ou mais unidades, passa a custar R$25.
    preco_teclado = 25
    # Criando a variável "preco_teclado" para calcular o preço do teclado. Cada teclado custa R$ 25 se comprados pelo menos uma dúzia.

else:
    # Se a condição acima for falsa (False), retorna verdadeiro (True). Caso seja comprado menos de 12 unidades, passa a custar R$30.
    preco_teclado = 30
    # Criando a variável "preco_teclado" para calcular o preço do teclado. Cada teclado custa R$ 30 se comprados menos do que uma dúzia.

# Criando a variável "preco_total" para calcular o preço dos teclados, multiplicando o "preco_teclado" e o "teclado_qtd", atribuindo o determinado preço para as quantidades informadas pelo usuário.
preco_total = preco_teclado * teclado_qtd

# Exibindo a quantidade de teclados comprados
print(f'A quantidade de teclados compradas foram de {teclado_qtd} unidades.')
# Utilizando a formatação de string para arredodar uma casa decimal. Por exemplo: ".1f" seria uma casa decimal e etc.
print(f'Valor total da compra: R${preco_total:.1f}')

