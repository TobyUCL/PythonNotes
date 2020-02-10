

from numpy import loadtxt

dataset = loadtxt("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv", delimiter=",")
x = dataset[:,0:8]
y = dataset[:, 8]

from keras.models import Sequential
from keras.layers import Dense
from keras.activations import relu, elu

p = {
    'first_neuron': [12, 24, 48],
    'activation': ['relu', 'elu'],
    'batch_size': [10, 20, 30]
}

p = {
    'first_neuron': [12],
    'activation': ['relu'],
    'batch_size': [10]
}


import diabetis_class
this_diabetis_class = diabetis_class.class_diabetes()

import talos

t = talos.Scan(x=x, y=y, params=p, model=this_diabetis_class.diabetes, experiment_name='diabetes')