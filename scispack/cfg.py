"""This configuration module is a container for parameters and constants."""
import numpy as np

# This is a constant
ANSWER = 42

# This is a parameter container
# It is a dictionary because we want it to be updated at runtime
PARAMS = dict()


def set_default_params():
    """Initializes PARAMS with the default values"""

    global PARAMS
    PARAMS['chuck_norris_birthday'] = ("Chuck Norris is immortal and doesn't "
                                       "have a birthday. But if he did, it "
                                       "would be today.")
    PARAMS['age_of_chuck_norris'] = 21  # because  is always 21
    PARAMS['pi'] = np.pi


# Make sure they are set at first import
set_default_params()
