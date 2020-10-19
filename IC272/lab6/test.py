import tensorflow as tf
from os import environ

environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

mat = tf.Variable([[1,2],[3,5]],tf.int32)
print("##########################################################################################")
print(mat[1],tf.rank(mat))