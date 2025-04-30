import pandas as pd
import os

# Caminho do arquivo na pasta 'data/raw'
file_path = os.path.join('C:/', 'PythonProjects', 'estudocd1', 'data', 'raw', 'ghostdata.csv')

# Lê o arquivo CSV
df = pd.read_csv(file_path)

# Realize algum processamento nos dados (exemplo)
df_processed = df.dropna()  # Exemplo de remover valores ausentes

# Caminho para salvar o arquivo processado
processed_file_path = os.path.join('C:/', 'PythonProjects', 'estudocd1', 'data', 'processed', 'dados_processados.csv')

# Salva o DataFrame processado na pasta 'data/processed'
df_processed.to_csv(processed_file_path, index=False)

print(f"\nDados processados foram salvos em: {processed_file_path}")

# Exibe as 5 primeiras linhas do DataFrame
# print(df.head())

# Verifica as colunas
# print("\nColunas:", df.columns.tolist())

# Verifica o tipo de cada coluna
# print("\nTipos de dados:\n", df.dtypes)