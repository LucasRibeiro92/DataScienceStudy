import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
matplotlib.use("TkAgg")  # ou "Qt5Agg" se você tiver PyQt5

# Gera uma lista aleatória
data = [random.randint(1, 100) for _ in range(30)]

fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(data)), data, align="edge")

ax.set_xlim(0, len(data))
ax.set_ylim(0, max(data) * 1.1)
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

iteration = [0]

def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data

def update_fig(data_list, rects, iteration):
    for rect, val in zip(rects, data_list):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f"Passos: {iteration[0]}")

ani = animation.FuncAnimation(
    fig,
    func=update_fig,
    fargs=(bar_rects, iteration),
    frames=bubble_sort(data.copy()),
    interval=50,
    repeat=False
)

plt.show()
