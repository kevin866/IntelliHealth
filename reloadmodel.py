from keras.backend import dropout
import joblib
import pandas as pd
import numpy as np
import tensorflow as tf
model = tf.keras.models.load_model('saved_model/my_model')
model.save("my_model.h5")

