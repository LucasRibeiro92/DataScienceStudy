from statistics import *
from numpy.ma import average

exercicio1list = [3,7,5,9,6]

print(average(exercicio1list))
print(stdev(exercicio1list))
print(variance(exercicio1list))

"""
exercicio2list = [150, 155, 160, 145, 170]

print(variance(exercicio2list))
print(stdev(exercicio2list))

exercicio3list = [20, 22, 24, 19, 30, 26]

print(average(exercicio3list))
print(variance(exercicio3list))
print(stdev(exercicio3list))

ex4list1 = (2, 4, 6, 8, 10)
ex4list2 = (60, 65, 70, 75, 80)

def regressao_linear_simples(x, y):
    n = len(x)
    media_x = sum(x) / n
    media_y = sum(y) / n

    numerador = sum((x[i] - media_x) * (y[i] - media_y) for i in range(n))
    denominador = sum((x[i] - media_x) ** 2 for i in range(n))

    b1 = numerador / denominador
    b0 = media_y - b1 * media_x

    return b0, b1

slope, intercept = regressao_linear_simples(ex4list1, ex4list2)

print(slope, intercept)

ex7list2 = (2, 5, 6, 3, 4, 7)

print(variance(ex7list2))
print(stdev(ex7list2))
"""
