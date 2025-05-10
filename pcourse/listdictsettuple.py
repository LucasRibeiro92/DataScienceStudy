# Criando uma lista
numeros = [1, 2, 3, 4, 5]

# Adicionando um item
numeros.append(6)

# Acessando elementos
print(numeros[2])  # 3

# Alterando elementos
numeros[2] = 10

# Removendo elementos
numeros.remove(4)

# Contando a quantidade de elementos
print(len(numeros))  # 5

# Criando uma tupla
coordenadas = (10, 20)

# Acessando elementos
print(coordenadas[0])  # 10

# Criando um dicionário
dados = {"nome": "Lucas", "idade": 25}

# Acessando valor por chave
print(dados["nome"])  # Lucas

# Adicionando ou alterando um valor
dados["idade"] = 26

# Removendo um item
del dados["nome"]

# Verificando se uma chave existe
print("nome" in dados)  # False

# Criando um conjunto
numeros = {1, 2, 3, 4}

# Adicionando um elemento
numeros.add(5)

# Removendo um elemento
numeros.remove(2)

# Verificando se um elemento está no conjunto
print(3 in numeros)  # True
