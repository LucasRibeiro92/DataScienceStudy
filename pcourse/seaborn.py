import matplotlib.pyplot as plt

x = [20.5, 35.7, 42.1, 15.9, 29.0]
y = [3.0, 5.0, 7.5, 2.0, 4.0]

plt.scatter(x, y)
plt.title("Conta vs Gorjeta")
plt.xlabel("Valor da Conta")
plt.ylabel("Gorjeta")
plt.grid()
plt.show()