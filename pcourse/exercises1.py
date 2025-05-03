#Crie uma lista com 5 nomes e imprima o terceiro nome.
nomes = ["Lucas", "Matias", "Carla", "Mario", "Janaina"]
print(nomes[2])  # Carla

#Escreva uma função que receba um número e diga se ele é par ou ímpar.
def parouimpar(numero):
    if numero % 2 == 0:
        print("O número ", numero,  " é par")
    else:
        print("O número ", numero, " é impar")

parouimpar(23)

#Crie um dicionário com 3 produtos e seus preços. Mostre todos os produtos e preços.
# Criando o dicionário
produtos = {
    "Arroz": 5.99,
    "Feijão": 7.49,
    "Macarrão": 4.25
}

# Mostrando os produtos e seus preços
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco}")

#Crie um laço que imprima os números de 10 até 1.
contador=10
while contador >= 1:
    print("Contador ", contador)
    contador -= 1

#Crie um arquivo chamado minha_lista.txt e escreva 3 frases nele.
with open("C:/PythonProjects/estudocd1/data/processed/exemplo.txt", "w") as f:
    f.write("Esse é um exemplo.")
    f.write("Esse outro exemplo.")
    f.write("E esse o terceiro exemplo.")

with open("C:/PythonProjects/estudocd1/data/processed/exemplo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)



