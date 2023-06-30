from typing import List
import random

def prioritize_random(Y:List[str])->List[str]:
    """
    Return a random ranking of a list of names
    :param Y: List of strings. The names to be ranked
    :return: List of strings. The ranked names.
    """
    Y_shuffled = random.sample(Y, len(Y))
    return Y_shuffled
