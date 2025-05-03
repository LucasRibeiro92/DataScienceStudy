import matplotlib.pyplot as plt

idades = [20, 25, 30, 35, 40]
salarios = [2000, 2500, 3200, 4000, 5000]

plt.plot(idades, salarios)
plt.title("Salário por Idade")
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.grid()
plt.show()