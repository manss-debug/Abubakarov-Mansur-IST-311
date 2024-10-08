import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

# Загрузка данных
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Проверка размеров наборов
print(f'Размер обучающего набора: {x_train.shape}, Размер тестового набора: {x_test.shape}')