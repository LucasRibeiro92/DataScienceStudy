# 📦 Importações
import math
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import sympy as sp
#import pingouin as pg

'''
# --------------------------
# 🔢 1. Biblioteca `math`
print("Math:")
print("Raiz quadrada de 16:", math.sqrt(16))
print("Seno de pi/2:", math.sin(math.pi / 2))

# --------------------------
# 📐 2. NumPy - Vetores e álgebra linear
print("\nNumPy:")
v = np.array([1, 2, 3])
w = np.array([4, 5, 6])
print("Produto escalar:", np.dot(v, w))
print("Norma de v:", np.linalg.norm(v))

# --------------------------
# 📊 3. pandas + estatística descritiva
print("\nPandas:")
df = pd.DataFrame({'valores': [10, 20, 30, 40, 50]})
print(df.describe())

# --------------------------
# 📈 4. scipy.stats - Estatísticas e testes
print("\nSciPy Stats:")
a = [12, 15, 14, 10, 13]
b = [22, 25, 19, 18, 20]
t_stat, p_val = stats.ttest_ind(a, b)
print("T-test entre dois grupos:", f"T = {t_stat:.3f}, p = {p_val:.3f}")

# --------------------------
# 📉 5. statsmodels - Regressão linear simples
print("\nStatsmodels (Regressão Linear):")
x = np.arange(10)
print(x)
y = 2.5 * x + np.random.normal(0, 1, 10)
x_const = sm.add_constant(x)
model = sm.OLS(y, x_const).fit()
print(model.summary())

# --------------------------
# 🧪 6. pingouin - Testes com DataFrames
print("\nPingouin:")
df_ping = pd.DataFrame({'grupo': ['A']*5 + ['B']*5,
                        'valores': a + b})
ttest = pg.ttest(dv='valores', between='grupo', data=df_ping)
print(ttest)
'''
# --------------------------
# 🧠 7. SymPy - Álgebra simbólica
print("\nSymPy:")
x = sp.Symbol('x')
f = x**2 + 2*x + 1
print("Função:", f)
print("Derivada:", sp.diff(f, x))
print("Integral:", sp.integrate(f, x))
print("Simplificada:", sp.simplify((x+1)**2))
'''
# --------------------------
# ✅ Fim do script
'''