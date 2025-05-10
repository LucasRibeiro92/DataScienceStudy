import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
matplotlib.use("TkAgg")  # ou "Qt5Agg" se você tiver PyQt5

# Número de barras e curva
n = 200
x = np.linspace(-2 * np.pi, 2 * np.pi, n)
sine_curve = np.sin(x)

# Criamos alturas proporcionais à curva seno
heights = list(range(1, n + 1))
random.shuffle(heights)

# Normalizamos as alturas para caberem na curva seno
max_height = max(heights)
target_heights = sine_curve.clip(min=0)  # ignora partes negativas da curva
scaling = target_heights / max(target_heights)  # para escalar os valores
scaled_heights = [h * s for h, s in zip(heights, scaling)]  # alturas proporcionais

# Setup matplotlib
fig, ax = plt.subplots()
bar_width = (x[1] - x[0]) * 0.9
bars = ax.bar(x, scaled_heights, width=bar_width, bottom=0, color='tomato')

ax.plot(x, sine_curve, color='black', linewidth=1.5, label='y = sin(x)')
ax.set_xlim(min(x) - 0.5, max(x) + 0.5)
ax.set_ylim(-1.2, 1.2)
ax.set_title("Ordenação com barras abaixo da curva senoide", fontsize=14)
ax.legend()

iteration = [0]

# Insertion Sort com reescalonamento
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

def update_fig(arr, bars, iteration):
    # atualiza alturas escalonadas novamente
    scaled = [h * s for h, s in zip(arr, scaling)]
    for rect, h in zip(bars, scaled):
        rect.set_height(h)
    iteration[0] += 1

ani = animation.FuncAnimation(
    fig,
    func=update_fig,
    fargs=(bars, iteration),
    frames=insertion_sort(heights.copy()),
    interval=10,
    repeat=False
)

plt.tight_layout()
plt.show()
