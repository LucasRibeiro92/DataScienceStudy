from pymongo import MongoClient
import pandas as pd
import os

# Conectando ao servidor local
client = MongoClient("mongodb://localhost:27017/")

# Acessando o banco e a coleção
db = client["lojadb"]
collection = db["vendas"]

# Buscando todos os dados da coleção
dados = list(collection.find())

# Convertendo em DataFrame
df = pd.DataFrame(dados)

# Criando a pasta caso não exista
os.makedirs("C:/PythonProjects/estudocd1/data/processed", exist_ok=True)

# Salvando como CSV
df.to_csv("C:/PythonProjects/estudocd1/data/processed/dados_vendas.csv", index=False)
