"""Plenty of useful functions doing useful things."""

# Importing packages at the top of your script is not required, but considered
# good practice. The order doesn't matter, but here again the python police
# recommends to use the following order:
#   - standard library packages
#   - installed packages
#   - library modules
import time
import numpy as np
from scispack import cfg


def give_me_the_answer(question, clever=False):
    """This gives you the answer.

    Parameters
    ----------
    question: str
        the question you are asking.
    clever: bool, optional
        whether or not the answer should be clever or not

    Returns
    -------
    The answer
    """

    if not isinstance(question, str):
        raise ValueError('The question should be a string!')

    if clever:
        # Mh, maybe I should think about the answer twice
        time.sleep(1)

    return cfg.ANSWER


def area_of_circle(radius):
    """Computes the area of a circle of radius `radius`.

    Parameters
    ----------
    radius: float
        the circle's radius

    Returns
    -------
    the circe's area (float)
    """

    return np.pi * radius**2
