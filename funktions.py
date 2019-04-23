import tensorflow.keras as keras
import tensorflow as tf
import pickle
import numpy as np
import cv2

def create_model():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(1000, activation=tf.nn.relu, input_shape=(1000,)))
    model.add(tf.keras.layers.Dense(900, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(800, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(700, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(600, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(4, activation=tf.nn.softmax))
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    return model

def image_processing(frame):
    # percent of original size
    scale_percent = 50
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    # cut image
    cutTop = 22
    cutLeft = 46
    frame = frame[cutTop:len(frame)-cutTop, cutLeft:len(frame[0])-cutLeft]
    # show borders
    frame = cv2.Canny(frame, 200,200)
    return np.array(frame)
