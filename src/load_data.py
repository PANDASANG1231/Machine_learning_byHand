import os
import numpy as np
from random import randint


def gen_data(low, high, n_rows, n_cols=None, seed=123):
    """Generate dataset randomly.
    Arguments:
        low {int} -- The minimum value of element generated.
        high {int} -- The maximum value of element generated.
        n_rows {int} -- Number of rows.
        n_cols {int} -- Number of columns.
    Returns:
        list -- 1d or 2d list with int
    """
    
    np.random.seed(seed)
    
    
    if n_cols is None:
        ret = low + (high - low) * np.random.rand(n_rows, 1)
    else:
        ret = low + (high - low) * np.random.rand(n_rows, n_cols)
    return ret