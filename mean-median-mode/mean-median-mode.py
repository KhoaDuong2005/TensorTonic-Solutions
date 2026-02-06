import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)
    mode = Counter(x).most_common(1)
    mode = mode[0][0]

    mean, median, mode = float(mean), float(median), float(mode)

    return mean, median, mode