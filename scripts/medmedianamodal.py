import statistics
from numpy.ma import average

conjunto = [4, 5, 6, 7, 8, 8, 9, 10, 10, 10]

#Media
media = average(conjunto)
print(f"A média dos elementos do conjunto é: {media:.2f}")

# Mediana
mediana = statistics.median(conjunto)
print("Mediana:", mediana)

# Moda
moda = statistics.mode(conjunto)
print("Moda:", moda)

conjunto.append(100)

media = average(conjunto)
print(f"A média dos elementos do conjunto é: {media:.2f}")
