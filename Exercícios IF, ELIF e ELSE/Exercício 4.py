# Questão 04) Faça um programa que pede para o usuário escrever uma letra qualquer e mostre na tela se ele digitou uma vogal ou uma consoante ou outro carácter.

# Pedindo ao usuário para digitar uma letra, utilizando a classe str. 
# Utilizando o método .lower() para converter a variável "letra_qualquer" para minúscula e o método .strip() para remover espaços extras.
letra_qualquer = str(input('Digite uma letra qualquer: ')).lower().strip()

# Utilizando a estrutura condicional IF, ELIF e ELSE para determinar se o letra é uma vogal, consoante ou outro carácter.
if letra_qualquer in "aáàãâeéêíîìioôõóòuûúù":
    # Utilizando o operador de associação "in" para a condição retornar verdadeira (True). Caso a letra seja encontrada, imprime a mensagem informando que é uma vogal.
    print(f'A letra {letra_qualquer} é uma vogal.')
elif letra_qualquer in "bcdfghjklmnpqrstvxwyz":
    # Se a condição acima for falsa (False), utiliza o operador de associação "in" para a condição retornar verdadeira (True). Caso a letra seja encontrada, imprime a mensagem informando que é uma consoante.
    print(f'A letra {letra_qualquer} é uma consoante.')
else:
    # Se as condições acima forem falsas (False), retorna verdadeiro (True) e imprime a mensagem informando para digitar apenas letras.
    print(f'Por favor, digite apenas letras.')

