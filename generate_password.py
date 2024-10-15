import random

print("Bem vindo ao seu Gerador de Senhas")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXXYZ~!@#$%^&*()<>?0123456789"

number = input("Numero de senhas geradas:")
number = int(number)

lenght = input("Quantidade de caracteres que terá sua senha: ")
lenght = int(lenght)

print("\n Aqui estao suas senhas: ")

for pwd in range(number):
    passwords = ""

    for c in range(lenght):
        passwords += random.choice(chars)
    
    print(passwords)
