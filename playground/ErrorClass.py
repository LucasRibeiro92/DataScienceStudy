# Definindo uma exceção personalizada
class NumeroNegativoError(Exception):
    pass

# Função que usa essa exceção
def processar_numero(n):
    if n < 0:
        raise NumeroNegativoError("Número negativo não é permitido!")
    return n ** 0.5

# Usando try/except com ela
try:
    resultado = processar_numero(-4)
except NumeroNegativoError as e:
    print(f"Erro personalizado: {e}")