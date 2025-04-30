import numpy as np
import matplotlib.pyplot as plt

def desenhar_grafico_linear(a, b, raiz):
    x = np.linspace(raiz - 10, raiz + 10, 400)
    y = a * x + b

    plt.figure(figsize=(8, 6))
    plt.axhline(0, color='gray', linewidth=1)
    plt.axvline(0, color='gray', linewidth=1)
    plt.plot(x, y, label=f"{a}x + {b}")
    if isinstance(raiz, (int, float)):
        plt.plot(raiz, 0, 'ro', label="Raiz")
    plt.title("Gráfico da Equação Linear")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def desenhar_grafico_seggrau(a, b, raiz):
    x = np.linspace(raiz - 10, raiz + 10, 400)
    y = a * x + b

    plt.figure(figsize=(8, 6))
    plt.axhline(0, color='gray', linewidth=1)
    plt.axvline(0, color='gray', linewidth=1)
    plt.plot(x, y, label=f"{a}x + {b}")
    if isinstance(raiz, (int, float)):
        plt.plot(raiz, 0, 'ro', label="Raiz")
    plt.title("Gráfico da Equação Linear")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Resolução de Equações Lineares do tipo ax + b = 0")
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        resultado = resolver_equacao_linear(a, b)
        print("\nResultado:")
        print("Raiz da equação:" if isinstance(resultado, (int, float)) else "Resultado:", resultado)

        if isinstance(resultado, (int, float)):
            desenhar_grafico(a, b, resultado)

    except ValueError:
        print("Entrada inválida. Por favor, digite números.")

if __name__ == "__main__":
    main()