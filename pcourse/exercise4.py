import random

# Criando uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([x for x in numeros if x % 2 != 0])

# Criando uma tupla
meses = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")

print(meses[2])

# Criando um dicionário
dados = {"nome": "Lucas", "idade": 25, "profissao": "Cientista de dados"}

# Adicionando ou alterando um valor
dados["idade"] = 32

dados["endereco"] = "Paulo Aquiles Malvezzi, 345"

# Acessando valor por chave
print(dados)  # Lucas

# Criando um conjunto
hora = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
minuto = {0, 15, 30, 45}
ampm = {"am", "pm"}

print(f"{random.choice(list(hora))}:{random.choice(list(minuto))} {random.choice(list(ampm))}")


