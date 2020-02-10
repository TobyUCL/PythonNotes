

from numpy import loadtxt

dataset = loadtxt("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv", delimiter=",")
x = dataset[:,0:8]
y = dataset[:, 8]

from keras.models import Sequential
from keras.layers import Dense
from keras.activations import relu, elu

p = {
    'first_neuron': [12, 24],
    'activation': ['relu', 'elu'],
    'batch_size': [10, 20]
}

def diabetes(x_train, y_train, x_val, y_val, params):
    
    # replace the hyperparameter inputs with references to params dictionary 
    model = Sequential()
    model.add(Dense(params['first_neuron'], input_dim=8, activation=params['activation']))
    #model.add(Dense(8, activation=params['activation']))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # make sure history object is returned by model.fit()
    out = model.fit(x=x_train, 
                    y=y_train,
                    validation_data=[x_val, y_val],
                    epochs=100,
                    batch_size=params['batch_size'],
                    verbose=0)
    
    # modify the output model
    return out, model

import talos

t = talos.Scan(x=x, y=y, params=p, model=diabetes, experiment_name='diabetes')