import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.random.uniform(-3, 3)
b = np.random.uniform(-3, 3)
c = np.random.uniform(-3, 3)

n = 100
x1 = np.random.randn(n)
x2 = np.random.randn(n)
z = np.random.randn(n) * 0.5
y = a + b * x1 + c * x2 + z

X = np.column_stack((x1, x2))
X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()
print(f'(a): {results.params[0]:.3f}')
print(f'(b): {results.params[1]:.3f}')
print(f'(c): {results.params[2]:.3f}')

x1_surf, x2_surf = np.meshgrid(np.linspace(x1.min(), x1.max(), 30),
                               np.linspace(x2.min(), x2.max(), 30))
X_surf = np.column_stack((x1_surf.ravel(), x2_surf.ravel()))
X_surf = sm.add_constant(X_surf)
y_surf = results.predict(X_surf).reshape(x1_surf.shape)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, x2, y, color='blue')
ax.plot_surface(x1_surf, x2_surf, y_surf, color='red', alpha=0.5)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.show()