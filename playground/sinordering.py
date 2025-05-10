import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
matplotlib.use("TkAgg")  # ou "Qt5Agg" se você tiver PyQt5

# Parâmetros
n = 100  # número de barras
data = list(range(1, n + 1))
random.shuffle(data)

# Geração de curva senoide para posicionar as barras
x = np.linspace(0, 2 * np.pi, n)
sine_y = np.sin(x)

fig, ax = plt.subplots()
bar_rects = ax.bar(x, data, width=0.05, bottom=sine_y, align='center', color='skyblue')
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(min(sine_y), max(sine_y) + n)

iteration = [0]

# Insertion Sort como gerador
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key
        yield arr

def update_fig(data_list, rects, iteration):
    for rect, h in zip(rects, data_list):
        rect.set_height(h)
    iteration[0] += 1

ani = animation.FuncAnimation(
    fig,
    func=update_fig,
    fargs=(bar_rects, iteration),
    frames=insertion_sort(data.copy()),
    interval=10,
    repeat=False
)

plt.title("Insertion Sort com barras sobre senoide")
plt.show()
