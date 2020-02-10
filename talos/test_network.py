"""
simple network class that should work
"""

import talos
import pandas as pd
## Model Prep
from talos.utils import lr_normalizer

from keras.models import Sequential
from keras.layers import Dropout, Dense

class classy_network():

    def iris_model(x_train, y_train, x_val, y_val, params):
    
        model = Sequential()                            
        model.add(Dense(params['first_neuron'],
                        input_dim=x_train.shape[1],
                        activation='relu'))
        
        model.add(Dropout(params['dropout']))
        model.add(Dense(y_train.shape[1],
                        activation=params['last_activation']))

        model.compile(optimizer=params['optimizer'](lr=lr_normalizer(params['lr'], params['optimizer'])),
                    loss=params['loss'],
                    metrics=['acc'])

        out = model.fit(x_train, y_train,
                        batch_size=params['batch_size'],
                        epochs=params['epochs'],
                        verbose=0,
                        validation_data=[x_val, y_val])
    
        return out, model