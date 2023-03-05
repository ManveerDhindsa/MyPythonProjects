import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import matplotlib.pyplot as plt
import math
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_hub as hub
import tensorflow_datasets as tfds
import numpy as np
from sklearn.metrics import roc_curve
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_examples = 7969
test_examples = 720
validation_examples = 992

img_height = img_width = 224
BATCH_SIZE = 32

model = keras.Sequential([
    hub.KerasLayer('https://tfhub.dev/google/imagenet/nasnet_mobile/feature_vector/5',
                   trainable=True),
    layers.Dense(1, activation='sigmoid'),
])

train_datagen = ImageDataGenerator(
    rescale = 1.0/255,
    rotation_range = 15,
    zoom_range = (0.95, 0.95),
    data_format = 'channels_last',
    # dtype = tf.float32,
)

validation_datagen = ImageDataGenerator(rescale=1.0/255)
test_datagen = ImageDataGenerator(rescale=1.0/255)

train_gen = train_datagen.flow_from_directory(
    'data/train/',
    target_size=(img_height, img_width),
    batch_size = BATCH_SIZE,
    color_mode = 'rgb',
    class_mode = 'binary',
    shuffle = True,
    seed = 123,
)

validation_gen = validation_datagen.flow_from_directory(
    'data/validation/',
    target_size=(img_height, img_width),
    batch_size = BATCH_SIZE,
    color_mode = 'rgb',
    class_mode = 'binary',
    shuffle = True,
    seed = 123,
)

test_gen = test_datagen.flow_from_directory(
    'data/test/',
    target_size=(img_height, img_width),
    batch_size = BATCH_SIZE,
    color_mode = 'rgb',
    class_mode = 'binary',
    shuffle = True,
    seed = 123,
)

model.load_weights('saved_model/')
model.compile(
    optimizer = keras.optimizers.Adam(lr=3e-4),
    loss = [keras.losses.BinaryCrossentropy(from_logits=False)],
    metrics=['accuracy']
)

model.fit(
    train_gen,
    epochs=2, 
    # steps_per_epoch=train_examples//BATCH_SIZE,
    steps_per_epoch=100,
    validation_data = validation_gen,
    validation_steps = validation_examples//BATCH_SIZE,
)

model.evaluate(validation_gen, verbose=2)
model.evaluate(test_gen, verbose=2)

model.save_weights('saved_model/')
# model.save('complete_saved_model/')