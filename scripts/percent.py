#Funções de c alculo de porcentagem e variação
def porcentagem(x, y):
    return (y / 100) * x

def aumentopercentual(x, y):
    return x * (1 + (y / 100))

def descontopercentual(x, y):
    return x * (1 - (y / 100))

def variacaopercentual(x, y):
    return abs(((y - x) / x) * 100)

print(porcentagem(250, 12))
print(aumentopercentual(500, 10))
print(descontopercentual(80, 20))
print(variacaopercentual(1800, 2160))
print(variacaopercentual(120, 90))
