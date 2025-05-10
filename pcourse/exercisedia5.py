from functools import reduce

#Crie uma função que receba um número e retorne se ele é par ou ímpar.
def evenorodd(x):
    if x % 2 == 0:
        return f"É par"
    else:
        return f"É impar"

print(evenorodd(783456))

#Use map() com lambda para elevar uma lista de números ao quadrado.
numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x * x, numeros))
print(quadrados)

#Use filter() com lambda para extrair apenas os nomes com mais de 5 letras de uma lista.
nomes = ["Lucas", "Ana", "Pedro", "Cleber", "Matias"]
maisde6letras = list(filter(lambda x: len(x) > 5, nomes))
print(maisde6letras)

#Use reduce() para multiplicar todos os itens de uma lista.
produtoReduce = reduce(lambda x, y: x * y, numeros)
print(produtoReduce)