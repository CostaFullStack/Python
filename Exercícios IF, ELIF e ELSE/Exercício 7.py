# Questão 07) Faça um programa que pede para o usuário escrever uma cor e mostre “Pare” se for vermelho, “Atenção” se for amarelo “Acelera” se for verde e “Cor inválida” se for qualquer outra.

# Pedindo ao usuário para digitar uma cor, utilizando a classe str. 
# Utilizando o método .lower() para converter a variável "cor_semaforo" para minuscula e o método .strip() para remover espaços extras.
cor_semaforo = str(input("""
Escolha uma cor:
                         
==> Vermelho
==> Amarelo
==> Verde  
                         
""")).lower().strip()

# Utilizando a estrutura condicional IF, ELIF e ELSE para determinar se a cor é Vermelha, Amarela ou Verde.
if cor_semaforo == "vermelho":
    # Utilizando o operador de comparação "==" para a condição retornar verdadeira (True). Caso a cor seja igual (==) a vermelho, imprime a mensagem pare.
    print(f'Pare!')
elif cor_semaforo == "amarelo":
    # Se a condição acima for falsa (False), utiliza o operador de comparação "==" para a condição retornar verdadeira (True). Caso a cor seja igual (==) a amarelo, imprime a mensagem atenção.
    print(f'Atenção!')
elif cor_semaforo == "verde":
    # Se as condições acima forem falsas (False), utiliza o operador de comparação "==" para a condição retornar verdadeira (True). Caso a cor seja igual (==) a verde, imprime a mensagem acelera.
    print(f'Acelera!')
else:
    # Se as condições acima forem falsas (False), retorna verdadeira (True) e imprime a mensagem informando que a cor é inválida.
    print(f'Cor inválida!')
    

