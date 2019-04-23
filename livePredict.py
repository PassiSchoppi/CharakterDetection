import funktions
import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import time
import cv2

cv2.namedWindow("preview")

# change folowing number if its not the main camera
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

# Restore the weights
model = funktions.create_model()
model.load_weights('./checkpoints/my_checkpoint')

i = 0
while rval:
    rval, frame = vc.read()
    frame = funktions.image_processing(frame)
    frame = tf.keras.utils.normalize(frame)
    # show
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)
    pred = model.predict(frame[np.newaxis, ...])
    predicted_class = np.argmax(pred[0], axis=-1)
    if predicted_class == 1:
        output = 'H'
    elif predicted_class == 2:
        output = 'U'
    elif predicted_class == 3:
        output = 'S'
    else:
        output = '_'
    print('predicted: '+str(output), end='\r')
    # time.sleep(0.5)
    i += 1
