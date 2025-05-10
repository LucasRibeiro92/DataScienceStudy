import csv

# Forma simples de abrir e ler um arquivo texto
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

# Cria ou sobrescreve um arquivo
with open("resultado.txt", "w") as arquivo:
    arquivo.write("Este é o novo conteúdo.\nNova linha adicionada.")

#Adicionando conteúdo ao arquivo
with open("resultado.txt", "a") as arquivo:
    arquivo.write("\nAdicionando mais conteúdo.")

#Lendo arquivos linha a linha
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # .strip() remove quebras de linha

#Lendo arquivos linha a linha /  Lendo arquivos .csv com a biblioteca csv
with open("exemplo.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)

# Lendo arquivos linha a linha /  Lendo arquivos .csv com a biblioteca csv e lidando com cabeçalho
with open("exemplo.csv", "r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        print(linha["nome"], linha["idade"])