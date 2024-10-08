import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)

x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='red')
plt.title('Heart Shape')
plt.axis('equal')
plt.axis('off')
plt.show()