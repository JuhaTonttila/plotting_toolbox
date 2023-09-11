
import numpy as np
# Contains random utility functions

def closest(array, value):
    # Find the index in array which has the closest value to "value"

    mintmp = np.abs(array-value)
    return np.where( mintmp == np.min(mintmp))[0][0]
