import tensorflow as tf
import os, numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
from dataset import get_data

_mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = _mnist.load_data()

zero_image = list(np.zeros((28,28), np.uint8))

class Network:
    def __init__(self) -> None:
        if (os.path.isfile("./model.h5")):
            self.model = tf.keras.models.load_model('./model.h5')
            return

        x_train, y_train = get_data()

        
        self.create_model()
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(x_train, y_train, epochs=10)
        
        self.model.save('model.h5')



    def create_model(self):
        self.model = Sequential()
        self.model.add(Conv2D(28, kernel_size=(3,3), input_shape=(28,28,1)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Flatten()) # Flattening the 2D arrays for fully connected layers
        self.model.add(Dense(128, activation=tf.nn.relu))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(10,activation=tf.nn.softmax))

        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    def predict(self, img):
        img = cv2.imread(img, 0)
        (_, img) = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
        images = []

        tile_size_i = int(img.shape[0] / 9)
        tile_size_j = int(img.shape[1] / 9)


        for i in range(0, img.shape[0]-tile_size_i, tile_size_i):
            for j in range(0, img.shape[1]-tile_size_j, tile_size_j):
                _img = img[i:i+tile_size_i, j:j+tile_size_j]
                _img = cv2.resize(_img, (28,28))
                images.append(_img)
                # cv2.imshow("", images[-1])
                # cv2.waitKey()


        img = np.invert(np.array(images))
        prediction = self.model.predict(img)
        return np.argmax(prediction, axis=1).reshape((9,9))

network = Network()
print(network.predict("./sudoku.jpg"))



