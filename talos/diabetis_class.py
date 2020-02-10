from keras.activations import relu, elu
from keras.models import Sequential
from keras.layers import Dense

class class_diabetes():
    def diabetes(self, x_train, y_train, x_val, y_val, params):
        
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