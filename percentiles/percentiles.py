import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x = np.sort(x)
    x = np.asarray(x)

    result = []
    for i in q:
        result.append(np.percentile(x, i))
    result = np.asarray(result)
    return result