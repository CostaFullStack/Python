# Questão 15) Você está desenvolvendo um sistema degerenciamento de estoque para uma loja deeletrônicos. Crie um dicionário chamado estoque com quantidades iniciais para 'Smartphone', 'Notebook' e 'Fones de ouvido'. Simule a adição e remoção de unidades destes produtos no estoque. Ao final, imprima o estado final do estoque.

# Criando um dicionário com nome "estoque".
estoque = {
# Utilizando a classe "str" e adicionando as "chaves" com seus respectivos "valores", utilizando a classe "str" contendo números com a classe "int".
'Smartphone': 15, 
'Notebook': 25, 
'Fones de ouvido': 30
}

# Iniciando com a estrutura de repetição "while" e utilizando um booleano (True) para se repetir até que o usuário digite a opção de sair.
while True:
    try:
        # Criando uma variável menu, utilizando a classe int e pedindo para o usuário digitar uma das opções abaixo.
        menu = int(input("""
    Escolha uma das opções abaixo:
    1 - Ver estoque
    2 - Adicionar produto
    3 - Remover produto
    0 - Sair
                        
    """))
        # Utilizando match e case para fazer as operações.
        match menu:
            # Se o usuário digitar o número '1'do menu, será feita a realização do estoque atual.
            case 1:
                # Utilizando o operador de associação "in" e utilizando a estrutura de repetição FOR para percorrer sobre a "chave" e o "valor" do dicionário.
                # Utilizando o método ".items()" para percorrer sobre as "chaves" e "valores".
                for nome, quantidade in estoque.items():
                    # Mostrando na tela os dados do estoque chamando o nome do dicionário e utilizando suas respectivas "chaves" e "valores". 
                    print(f"""
    Nome do produto: {nome}
    Quantidade disponível: {quantidade} unidades
    """) 
            # Se o usuário digitar o número '2'do menu, será feita a realização da adição de unidades ao determinado produto.
            case 2:
                # Pedindo ao usuário para digitar nome e a quantidade do produto, utilizando a classe "str" e "int". 
                nome_produto = str(input('Digite o nome do produto que deseja adicionar mais unidades: '))
                qtd_produto = int(input(f'Digite a quantidade do produto {nome_produto}: '))
                # Utilizando a estrutura condicional IF e ELSE para determinar se o nome está ou não no dicionário "estoque".
                # Utilizando o operador de associação "in" para a condição retornar verdadeira (True).
                if nome_produto in estoque:
                    # Adicionando o nome do produto digitado na variável "nome_produto" como "chave" no dicionário "estoque" e realizando a soma das undidades na variável "qtd_produto" como "valor".
                    estoque[nome_produto] += qtd_produto
                    # Mostrando na tela o nome do produto com a unidade adicionada.
                    print(f'{qtd_produto} unidades do produto "{nome_produto}" adicionadas com sucesso!')                   
                # Caso o usuário digite na variável "nome_produto" um nome que não esteja no dicionário "estoque", uma mensagem de produto não encontrado aparece.            
                else:
                    print(f'Produto "{nome_produto}" não encontado no estoque!')
            case 3:
                # Pedindo ao usuário para digitar nome e a quantidade do produto, utilizando a classe "str" e "int". 
                nome_produto = str(input('Digite o nome do produto que deseja remover: '))
                qtd_produto = int(input(f'Digite a quantidade do produto {nome_produto} que deseja remover: '))
                # Utilizando a estrutura condicional IF e ELSE para determinar se o nome está ou não no dicionário "estoque".
                # Utilizando o operador de associação "in" para a condição retornar verdadeira (True).
                # Utilizando o operador lógico "and" para a condição retornar verdadeira (True) se ambas as afirmações forem verdadeiras. Caso a quantidade de unidades da chave no dicionário "estoque[nome_produto]" seja maior ou igual (>=) que as unidades do valor "qtd_produto", imprime a mensagem informando que as unidades do produto foram removidas.
                if nome_produto in estoque and estoque[nome_produto] >= qtd_produto:
                    # Adicionando o nome do produto digitado na variável "nome_produto" como "chave" no dicionário "estoque" e realizando a subtração das unidades na variável "qtd_produto" como "valor".
                    estoque[nome_produto] -= qtd_produto
                    # Mostrando na tela o nome do produto com a unidade removida.
                    print(f'{qtd_produto} unidades do produto "{nome_produto}" removidas com sucesso!')
                # Caso o usuário digite na variável "qtd_produto" uma quantidade que seja maior que a do dicionário "estoque", uma mensagem de unidades não suficientes no estoque.        
                else:
                    print(f'Não há {qtd_produto} unidades de "{nome_produto}" suficientes no estoque!')    
            # Se o usuário digitar o número '0' do menu, o loop será encerrado.       
            case 0:
                print('Programa encerrado. Volte sempre!')
                break
                # Encerrando o loop.
            # Se o usuário digitar um número que não está no menu, aparecerá uma mensagem de erro.
            case _:
                print('Opção inválida. Por favor, selecione uma opção válida!')
    # Se o usuário não digitar números, aparecerá uma mensagem de erro.
    except ValueError:
        print('Digite apenas números!')

