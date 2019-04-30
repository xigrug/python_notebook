import numpy as np
delta = 0.5
x = np.arange(-3.0, 4.001, delta)
print(x)
y = np.arange(-4.0, 3.001, delta)
print(y)
X, Y = np.meshgrid(x, y)
print(X)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
print(Z)
