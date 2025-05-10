import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
matplotlib.use("TkAgg")  # ou "Qt5Agg" se você tiver PyQt5

# ======================= CONFIGURAÇÕES =======================

NUM_BARS = 100             # <-- Aumente ou diminua a quantidade de barras
SPEED_MS = 30             # <-- Velocidade da animação em milissegundos (menor = mais rápido)
ALLOW_DUPLICATES = 1      # <-- 0 = pode repetir altura, 1 = todos os valores únicos

BAR_COLOR = "#60e47c"     # <-- Cor das barras
BG_COLOR = "#373737"      # <-- Cor do fundo
BAR_EDGE_COLOR = "#ffffff"  # <-- Cor da borda da barra
TEXT_COLOR = "#e1e1e1"    # <-- Cor do texto dos passos

# ======================= GERA DADOS =======================

if ALLOW_DUPLICATES:
    # Gera valores únicos embaralhados
    data = list(range(1, NUM_BARS + 1))
    random.shuffle(data)
else:
    # Gera com possíveis valores repetidos
    data = [random.randint(1, 100) for _ in range(NUM_BARS)]

# ======================= CONFIGURAÇÃO DO GRÁFICO =======================

fig, ax = plt.subplots()
fig.patch.set_facecolor(BG_COLOR)
bar_rects = ax.bar(range(len(data)), data, align="edge", color=BAR_COLOR, edgecolor=BAR_EDGE_COLOR)

ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, NUM_BARS)
ax.set_ylim(0, int(max(data) * 1.1))
ax.tick_params(axis='x', colors=TEXT_COLOR)
ax.tick_params(axis='y', colors=TEXT_COLOR)

text = ax.text(0.02, 0.95, "", transform=ax.transAxes, color=TEXT_COLOR)

iteration = [0]

# ======================= ALGORITMO DE ORDENAÇÃO =======================

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            yield a

# ======================= FUNÇÃO DE ATUALIZAÇÃO =======================

def update_fig(updated_data, rects, iteration):
    for rect, val in zip(rects, updated_data):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f"Passos: {iteration[0]}")

# ======================= ANIMAÇÃO =======================

ani = animation.FuncAnimation(
    fig,
    func=update_fig,
    fargs=(bar_rects, iteration),
    frames=bubble_sort(data),
    interval=SPEED_MS,
    repeat=False
)

plt.show()
