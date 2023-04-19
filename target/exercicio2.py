# Exercicio 2
def fibonacci(numero):
    i, j = 0, 1
    lista = [0, 1]
    prox = 0
    while True:
        if prox > numero:
            print(f"O número {numero} NÃO está na Sequência de Fibonacci")
            break
        elif numero in lis16ta:
            print(f"O número {numero} ESTÁ na Sequência de Fibonacci")
            break
        else:
            prox = lista[i]+ lista[j]
            i += 1
            j += 1
            lista.append(prox)


num_desejado = int(input("Digite o número que quer encontrar no Fibonacci: "))
fibonacci(num_desejado)