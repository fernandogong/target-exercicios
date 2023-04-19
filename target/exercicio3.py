# Exercicio 3
import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
    valores = [dia['valor'] for dia in dados if dia['valor'] != 0]
    dias_valor_maior = 0

    menor_valor = min(valores)
    maior_valor = max(valores)
    media_valor = sum(valores) / len(valores)

    for v in valores:
        if v > media_valor:
            dias_valor_maior += 1

    print(f'Menor valor: {menor_valor:.2f}')
    print(f'Maior valor: {maior_valor:.2f}')
    print(f'{dias_valor_maior} dia(s) tiveram um faturamento diário superior à média mensal.')