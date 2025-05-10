import csv
from config import DATA_DIR

#Crie um arquivo .txt com uma mensagem sua e leia o conteúdo de volta no console.
# Cria ou sobrescreve um arquivo
with open(f"{DATA_DIR}/processed/resultado.txt", "w") as arquivo:
    arquivo.write("Arquivo criado ao estudar a manipulação de arquivos com Open nativo.\n")

# Lendo arquivos linha a linha
with open(f"{DATA_DIR}/processed/resultado.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # .strip() remove quebras de linha

#Escreva uma lista de números de 1 a 10, um por linha, em um arquivo texto.
with open(f"{DATA_DIR}/processed/resultadolista.txt", "w") as arquivo:
    for i in range(11):
        arquivo.write(f"{i}\n")

with open(f"{DATA_DIR}/processed/resultadolista.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # .strip() remove quebras de linha

#Leia esse arquivo linha a linha e transforme os dados em inteiros para somá-los.
value = 0
with open(f"{DATA_DIR}/processed/resultadolista.txt", "r") as arquivo:
    for linha in arquivo:
        numero = int(linha.strip())
        value += numero

print(value)

#Crie um arquivo .csv fictício com 3 colunas: nome, idade, cidade. Leia e imprima os dados formatados.
with open(f"{DATA_DIR}/processed/exemplo.csv", "r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for pessoa in leitor:
        print(f"{pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}.")