""" Define and interface for all models """


class MainModel:
    """ Defines methods to be implemented in the rnn and lstm classes
    """
    def __init__(self, x_input, y_output) -> None:
        """ Initializer for all variables

        Args:
            x_input (numpy matrix): represents the data input
            y_output (numpy matrix): represents the data model or ground truth
        """
        self.x_input = x_input
        self.y_output = y_output
    # define emply methods
    def base_model_func(self, input_args):
        """Define base model utils for training
        and defines all training parameters

        Args:
            input_args (dict or numpy array): contains all training parameters
        """

    