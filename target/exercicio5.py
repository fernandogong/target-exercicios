# Exercicio 5
lista = []

palavra = str(input("Digite uma palavra: "))

palavra_invertida = ""

for letra in palavra[::-1]:
    palavra_invertida += letra

print(palavra_invertida)