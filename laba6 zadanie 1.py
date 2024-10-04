from cProfile import label
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt

fahrenheit = [[-88.6], [-29.2], [32.0], [93.2], [129.2], [152.6], [212.0]]
kelvin = [[-67.0], [-34.0], [0], [34.0], [54.0], [67.0], [100]]
for c, f in zip(kelvin, fahrenheit):
    print(f'фаренгейт{c} = кельвин {f}')
lr = LinearRegression()
lr.fit(fahrenheit, kelvin)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
kelvin_test = [[-50], [10], [30], [20], [10], [70], [87]]
fahrenheit_test = lr.predict(kelvin_test)
fahrenheit_test
for c, f in zip(kelvin_test, fahrenheit_test):
    print(f'фаренгейт{c} = кельвин {f}')
x_range = np.arange(-70, 120)
y_range = (x_range - 273, 15) * 1, 8 + 32
plt.figure(figsize=(15, 8), dpi=280)
plt.plot(x_range, y_range, label='уравнение', linewidth='1')
plt.scatter(kelvin, fahrenheit, label='входные данные', color='green')
plt.scatter(kelvin_test, fahrenheit_test, label='предсказанное значение', color='blue')
plt.xlabel('Цельсия')
plt.ylabel('Фаренгейта')
plt.legend()
plt.grid(True)
plt.show()
