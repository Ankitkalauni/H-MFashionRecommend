import numpy as np
import pandas as pd

def precision_at_k(y_true, y_pred, k=12):
    """ Computes Precision at k for one sample
    
    Parameters
    __________
    y_true: np.array
            Array of correct recommendations (Order doesn't matter)
    y_pred: np.array
            Array of predicted recommendations (Order does matter)
    k: int, optional
       Maximum number of predicted recommendations
            
    Returns
    _______
    score: double
           Precision at k
    """
    intersection = np.intersect1d(y_true, y_pred[:k])
    return len(intersection) / k
