from cProfile import label
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
from sympy.printing.pretty.pretty_symbology import line_width

fahrenheit = [[-67.0], [-34.0], [0], [34.0], [54.0], [67.0], [100]]
kelvin = [[(f[0] - 32) * 5/9 + 273.15] for f in fahrenheit]
plt.figure(figsize=(15, 8), dpi=50)
plt.scatter(fahrenheit, kelvin, label='входные значения', color='green', marker='$f$');
plt.xlabel('fahrenhtein')
plt.ylabel('kelvin')
plt.legend()
plt.grid(True)
plt.show()
for c, f in zip(fahrenheit, kelvin):
    print(f'фаренгейт{c}= кельвин {f}')
lr = LinearRegression()
lr.fit(fahrenheit, kelvin)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
fahrenheit_test = [[-50], [10], [30], [20], [10], [70], [87]]
kelvin_test = lr.predict(fahrenheit_test)
kelvin_test
for c, f in zip(fahrenheit_test,kelvin_test):
    print(f'фаренгейта{c} кельвин{f}')
x_range = np.arange(-70, 120)
y_range = (x_range - 32) * 5/9 + 273.15
plt.figure(figsize=(15, 8), dpi=280)
plt.plot(x_range, y_range, label='уравнение', linewidth=1)
plt.scatter(fahrenheit,kelvin, label='входные данные', color='green')
plt.scatter(fahrenheit_test,kelvin_test, label='предсказанное значение', color='blue')
plt.xlabel('Фаренгейт')
plt.ylabel('Кельвин')
plt.legend()
plt.grid(True)
plt.show()
