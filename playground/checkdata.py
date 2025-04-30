import pandas as pd
import os

# Caminho para o arquivo processado
file_path = os.path.join('C:/', 'PythonProjects', 'estudocd1', 'data', 'processed', 'dados_processados.csv')

# Lê o arquivo CSV
df_processed = pd.read_csv(file_path)

# Calcula o número de valores únicos por coluna
valores_distintos_por_coluna = df_processed.nunique()


# Exibe o número de valores distintos por coluna
print("Número de valores distintos por coluna:")
print(valores_distintos_por_coluna)


"""
# Se você quiser ver os valores únicos de cada coluna
for coluna in df_processed.columns:
    print(f"\nValores únicos na coluna '{coluna}':")
    print(df_processed[coluna].unique())
"""