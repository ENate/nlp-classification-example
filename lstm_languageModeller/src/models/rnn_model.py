""" An implementation of recurrent neural network example """
# Imports
import numpy as np


def rnn_model(input_data, output_data):
    """Implementation of the recurrent neural network
    training model. Model input parameters: input and 
    output data sets.

    Args:
        input_data (array): represents the input data
        output_data (array): represents the output data
    """
    pass

class RNNs(rnn_model.MainModel):
    """ Defines a class for recurrent neural networks
    """
    
    def __init__(self, x, y) -> None:
        """Initialize all fields

        Args:
            x (numpy_array): input matrix of real numbers
            y (numpy_array): output data consisting of real numbers
        """
        self.x_input = x
        self.y_ouput = y
    
    def hidden_step(self):
        """
        A function to update the hidden states
        and compute the output vector of rnns
        """
        # compute the output vector
        self.hid = np.tanh(np.dot(self.W_hh, self.hid) + np.dot(self.W_xh, self.input_x))
        self.y = np.dot(self.W_hy, self.hid)