
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from keras.models import Sequential
import tensorflow as tf


def model():
    cnn = Sequential()
    cnn.add(Conv2D(32, kernel_size=(5, 5), input_shape=(
        28, 28, 1), padding='same', activation='relu'))
    cnn.add(MaxPooling2D())
    cnn.add(Conv2D(64, kernel_size=(5, 5), padding='same', activation='relu'))
    cnn.add(MaxPooling2D())
    cnn.add(Flatten())
    cnn.add(Dense(1024, activation='relu'))
    cnn.add(Dense(10, activation='softmax'))
    cnn.compile('adam', loss='categorical_crossentropy', metrics=['accuracy'])

    cnn.load_weights('weight_cnn.h5')
    return cnn, tf.get_default_graph()
