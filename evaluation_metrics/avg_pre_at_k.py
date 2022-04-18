from precision_at_k import precision_at_k
from rel_at_k import rel_at_k
import numpy as np
import pandas as pd


def average_precision_at_k(y_true, y_pred, k=12):
    """ Computes Average Precision at k for one sample
    
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
           Average Precision at k
    """
    ap = 0.0
    for i in range(1, k+1):
        ap += precision_at_k(y_true, y_pred, i) * rel_at_k(y_true, y_pred, i)
        
    return ap / min(k, len(y_true))