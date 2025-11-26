from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

S0 = 0.99
I0 = 0.01
R0 = 0.0
y0 = [S0, I0, R0]

t = np.linspace(0, 50, 500)

Z = 0.3
V = 0.1

def sir_model(y, t, Z, V):
    S, I, R = y
    dS_dt = -Z * S * I
    dI_dt = Z * S * I - V * I
    dR_dt = V * I
    return [dS_dt, dI_dt, dR_dt]

solution = odeint(sir_model, y0, t, args=(Z, V))
S, I, R = solution.T

plt.plot(t, S, label='(S)')
plt.plot(t, I, label='(I)')
plt.plot(t, R, label='(R)')
plt.xlabel('t')
plt.ylabel('%')
plt.legend()
plt.grid()
plt.show()