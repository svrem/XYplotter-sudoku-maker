from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import normalize
import numpy as np

def get_data():
    _mnist = mnist
    (x_train, y_train), (x_test, y_test) = _mnist.load_data()

    where = np.where(y_train == 0)[0]
    x_train = list(x_train)
    y_train = list(y_train)


    offset = 0
    for i in where:
        del x_train[i-offset]
        del y_train[i-offset]
        offset += 1

    for _ in range(1000):
        x_train.append(list(np.zeros((28,28), np.uint8)))
        y_train.append(0)

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    
    print(x_train.shape)

    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

    x_train = normalize(x_train, axis=1)
    x_test = normalize(x_test, axis=1)

    return x_train, y_train