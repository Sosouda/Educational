import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path1 = 'Hydra04.xlsx'
file_path2 = 'OpBar.xlsx'

n_days = 6

x = np.zeros(n_days)
y = np.zeros(n_days)

for i in range(n_days):
    X = np.array(pd.read_excel(file_path1, skiprows=2 + i * 1441, usecols="C", nrows=1440))
    x[i] = np.mean(X)
#E для температуры
for i in range(n_days):
    Y = np.array(pd.read_excel(file_path2, skiprows=2 + i * 1441, usecols="D", nrows=1440))
    y[i] = np.mean(Y)
#Z для температуры

degree = 1
coefficients = np.polyfit(x, y, degree)

a1, a0 = coefficients

print(f"Коэффициенты аппроксимирующей функции: y = {a0:.4f} + {a1:.4f}x")

def linapprox(x):
    return a0 + a1 * x

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', s=50)

x_min, x_max = min(x) - 5, max(x) + 5
x_tch = np.linspace(x_min, x_max, 100)
y_tch = linapprox(x_tch)

plt.plot(x_tch, y_tch, label=f'Аппроксимация: y = {a0:.4f} + {a1:.4f}x', color='blue', linewidth=2)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()