# Exercicio 4
dados = [
    {
        "estado": "SP",
        "faturamento": 67386.43
    },
    {
        "estado": "RJ",
        "faturamento": 36678.66
    },
    {
        "estado": "MG",
        "faturamento": 29229.88
    },
    {
        "estado": "ES",
        "faturamento": 27165.48
    },
    {
        "estado": "OUTROS",
        "faturamento": 19849.53
    }
]

soma_faturamento = 0
for f in dados:
    soma_faturamento += f['faturamento']

for e in dados:
    print(f"{e['estado']} tem {e['faturamento']*100/soma_faturamento:.2f}% de representação")