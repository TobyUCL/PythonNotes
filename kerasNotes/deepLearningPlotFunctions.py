import numpy as np
import matplotlib.pyplot as plt


def loss_plot(history, network_name, file_extension = '.png'):
    """
    Plot saves and displays the training and validation loss

    Parameters
    ----------
    history : object
    this contains    history.history: dict
            contains the loss and validation loss over all of the epochs
    network_name : string
        the name of the network
    file_extension = '.png':
        the file extension other extensions are '.svg' or '.jpg'

    """

    number_epochs = len(history.history["loss"])
    plt.plot(np.arange(number_epochs), history.history["loss"], label = "loss")

    # there may be no validation data_set
    try:
        plt.plot(np.arange(number_epochs), history.history["val_loss"], label = "val_loss")
    except NameError:
        print("history.history[\"val_loss\"] is not defined.")
    
    plt.legend()
    plt.savefig(network_name+file_extension)
    plt.show()