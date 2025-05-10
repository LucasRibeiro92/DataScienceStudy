from collections import Counter

#Crie um dicionário com dados de um livro (título, autor, ano) e imprima os valores.
livro = {
    "titulo": "Data Science do Zero",
    "autor": "Joel Grus",
    "ano": 2021,
}
print(f"O livro se chama {livro['titulo']}. Foi escrito por {livro['autor']} e lançado no ano de {livro['ano']} ")

#A partir de uma lista com nomes repetidos, crie um set com nomes únicos.
nomes = ["Lucas", "Ana", "Pedro", "Cleber", "Matias", "Matias", "Matias", "Pedro"]
conjuntodenome = set(nomes)
print(conjuntodenome)

#Use set para descobrir quais números aparecem em duas listas diferentes.
numeros1 = {8, 3 ,4, 10, 9}
numeros2 = {1, 3, 4, 5, 7}
print(numeros1.intersection(numeros2))

#Escreva um programa que conte quantas vezes cada letra aparece em uma frase (usando dict).
frase = "Cientista de Dados é o futuro!"
frase = frase.lower()  # tudo minúsculo

contador = {}

for letra in frase:
    if letra.isalpha():  # só conta letras
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

# Exibir o dicionário
for letra, qtd in contador.items():
    print(f"{letra}: {qtd}")

#Versão moderna com collections.Counter
frase2 = "Cientista de Dados é o futuro!".lower()
letras = [letra for letra in frase2 if letra.isalpha()]  # compreensao de lista

contagem = Counter(letras)

for letra, qtd in contagem.items():
    print(f"{letra}: {qtd}")