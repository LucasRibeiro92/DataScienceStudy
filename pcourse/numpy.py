import numpy as np

# Criando arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Array a:", a)

# Operações
print("Soma:", a + 10)
print("Média:", np.mean(a))
print("Desvio padrão:", np.std(a))

# Array 2D (matriz)
matriz = np.array([[1, 2], [3, 4]])
print("Matriz 2x2:")
print(matriz)