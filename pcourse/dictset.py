#Dictionary
aluno = {
    "nome": "João",
    "idade": 25,
    "curso": "Python"
}

print(aluno["nome"])  # João

aluno["nota"] = 9.5            # Adiciona nova chave
print(aluno.get("cidade"))     # Retorna None se não existir

print(aluno.keys())            # Todas as chaves
print(aluno.values())          # Todos os valores
print(aluno.items())           # Pares chave:valor

#Set(Conjunto)
numeros = [1, 2, 2, 3, 4, 4, 4]
conjunto = set(numeros)

print(conjunto)  # {1, 2, 3, 4}

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))         # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))    # {1, 2}