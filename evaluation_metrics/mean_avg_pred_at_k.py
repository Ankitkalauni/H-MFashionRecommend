from avg_pre_at_k import average_precision_at_k

import numpy as np
import pandas as pd

def mean_average_precision(y_true, y_pred, k=12):
    """ Computes MAP at k
    
    Parameters
    __________
    y_true: np.array
            2D Array of correct recommendations (Order doesn't matter)
    y_pred: np.array
            2D Array of predicted recommendations (Order does matter)
    k: int, optional
       Maximum number of predicted recommendations
            
    Returns
    _______
    score: double
           MAP at k
    """
    return np.mean([average_precision_at_k(gt, pred, k) \
                    for gt, pred in zip(y_true, y_pred)])



if __name__ == "__main__":
        gt = np.array(['a', 'b', 'c', 'd', 'e'])
        preds1 = np.array(['b', 'c', 'a', 'd', 'e'])
        
        y_true = np.array([gt, gt, gt, gt, gt, gt])
        y_pred = np.array([preds1])
        print(average_precision_at_k(gt, preds1, k=4))