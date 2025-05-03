import pandas as pd

# Criando DataFrame manualmente
dados = {
    "Nome": ["Lucas", "Ana", "Pedro"],
    "Idade": [25, 32, 40],
    "Salario": [3000, 4200, 5000]
}

df = pd.DataFrame(dados)
print(df)

# Operações básicas
print("Média de salário:", df["Salario"].mean())
print("Pessoas com salário > 4000:")
print(df[df["Salario"] > 4000])

try:
    df = pd.read_csv("C:/PythonProjects/estudocd1/data/processed/dados_vendas.csv")# Ex: Titanic.csv
except FileNotFoundError as e:
    print(f"Arquivo não encontrado: {e.args}")

print(df.head())  # Mostra as 5 primeiras linhas