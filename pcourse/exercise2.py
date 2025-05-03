import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Criando arrays
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Média:", np.mean(a))
print("Soma:", np.sum(a))
print("Desvio padrão:", np.std(a))

# Dataframe
dados = {
    "Nome": ["Lucas", "Ana", "Pedro", "Cleber", "Matias"],
    "Matematica": [25, 32, 40, 65, 95],
    "Portugues": [70, 80, 74, 65, 90],
    "Historia": [94, 89, 99, 75, 100]
}

df = pd.DataFrame(dados)

# Calculando a média por aluno
df['Media'] = df[['Matematica', 'Portugues', 'Historia']].mean(axis=1)

# Mostrando o DataFrame com as médias
print(df)

x = np.array(df['Nome'])
y = np.array(df['Media'])

plt.bar(x, y)
plt.show()