# Questão 14) Crie um programa que gere e imprima os primeiros 10 termos da sequência de Fibonacci.


# Iniciando duas variáveis uma chamada "primeiro_termo" que inicia com 0 e a outra "segundo_termo" que inicia com 1 que são os dois primeiros termos da sequência Fibonacci e percorrer através da estrutura de repetição FOR.
primeiro_termo = 0
segundo_termo = 1

# Utilizando a estrutura de repetição FOR para iterar 10 vezes.
for _ in range(10):
    # Mostrando na tela o primeiro termo da sequência, no caso 0, e colocando espaço entre os números com o parâmetro "end".
    print(primeiro_termo, end= " ")
    # Criando uma variável "proximo_termo" e calculando o próximo termo da sequência com as variáveis "primeiro_termo" e "segundo_termo".
    proximo_termo = primeiro_termo + segundo_termo
    # A variável "primeiro_termo" se torna o "segundo_termo" e o "segundo_termo" se torna o "proximo_termo" que foi calculado.
    primeiro_termo, segundo_termo = segundo_termo, proximo_termo



