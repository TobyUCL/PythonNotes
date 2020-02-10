"""
How to check the layers in a keras model.
"""
import keras

network = keras.models.load_model("MNIST_network.h5")
"""
if your network contains a lambda function which uses tensorflow functions
"""
import tensorflow as tf
network = keras.models.load_model("MNIST_network.h5", custom_objects={'tf': tf})


# see the layers
print(network.layers)
num_layers = len(network.layers)

"""
Check the output from each layer
"""
inp = network.input                                           # input placeholder
outputs = [layer.output for layer in network.layers]          # all layer outputs