import numpy as np

polinomios = [
    ([3, -6], "3x -10 6"),
    ([-2, 8], "-2x + 8"),
    ([1, -10], "x - 10"),
    ([0.5, -1], "0.5x - 1"),
    ([4, 0], "4x + 0"),
    ([-7, -14], "-7x - 14"),
    ([2.3, 1.1], "2.3x + 1.1"),
    ([1, 1], "x + 1"),
    ([-1, -1], "-x - 1"),
    ([10, -100], "10x - 100")
]

def main():
    print("Escolha uma equação para resolver:")
    for i, (_, texto) in enumerate(polinomios, 1):
        print(f"{i}. {texto} = 0")

    try:
        escolha = int(input("\nDigite o número da equação (1-10): "))
        if 1 <= escolha <= len(polinomios):
            coef, texto = polinomios[escolha - 1]
            raizes = np.roots(coef)
            print(f"\nEquação escolhida: {texto} = 0")
            print("Solução:", raizes[0])  # só uma raiz
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()