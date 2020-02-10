import test_network 

classy_instance = test_network.classy_network()

import talos
import pandas as pd

## Data prep
x, y = talos.templates.datasets.iris()

## Model Prep
from talos.utils import lr_normalizer

from keras.models import Sequential
from keras.layers import Dropout, Dense

## Setting the parameter space
from keras.optimizers import Adam, Nadam
from keras.activations import softmax
from keras.losses import categorical_crossentropy, logcosh

p = {'lr': (0.1, 10, 10),
     'first_neuron':[4, 8, 16, 32, 64, 128],
     'batch_size': [2, 3, 4],
     'epochs': [200],
     'dropout': (0, 0.40, 10),
     'optimizer': [Adam, Nadam],
     'loss': ['categorical_crossentropy'],
     'last_activation': ['softmax'],
     'weight_regulizer': [None]}


## Run the hyperparameter scan
scan_object = talos.Scan(x,
                         y, 
                         params=p,
                         model=classy_instance.iris_model,
                         experiment_name='iris',
                         fraction_limit=.001)