# Questão 14) Implemente uma função chamada filtrar_emails que recebe uma lista de endereços de e-mail e retorna uma nova lista contendo apenas os e-mails do gmail.

lista_emails = [
"example1@gmail.com", 
"example2@hotmail.com", 
"example3@yahoo.com.br", 
"example4@gmail.com"
]

def filtar_emails(lista_emails):
    lista_gmails = []
    for email in lista_emails:
        if email.endswith("@gmail.com"):
            lista_gmails.append(email)
    return lista_gmails

resultado = filtar_emails(lista_emails)

print(f"Lista com apenas os e-mails do gmail:\n{resultado}")
