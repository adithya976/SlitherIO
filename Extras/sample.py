import tensorflow as tf
# from tensorflow.python import keras

tf.python.n

mnist=tf.keras.datasets.mnist
(x,y),(a,b)=mnist.load_data()
print("mnist dataset loaded")
print(x.shape)
print(y.shape)
print(a.shape)
print(b.shape)