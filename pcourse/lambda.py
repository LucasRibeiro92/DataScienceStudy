from functools import reduce

quadrado = lambda x: x * x
print(quadrado(4))  # 16

# map() → aplica uma função a todos os itens de uma lista:
numeros = [1, 2, 3, 4]
dobros = list(map(lambda x: x * 2, numeros))
print(dobros)  # [2, 4, 6, 8]

#filter() → filtra itens com base em uma condição:
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

#reduce() → reduz todos os valores a um único resultado (ex: soma):
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # 10