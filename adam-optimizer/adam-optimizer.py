import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    new_m = beta1 * m + (1 - beta1) * grad
    new_v = beta2* v + (1 - beta2) * grad**2
    bias_corrected_m = new_m / (1 - beta1**t)
    bias_corrected_v = new_v / (1 - beta2**t)
    param_new = param - lr *(bias_corrected_m / (np.sqrt(bias_corrected_v) + eps))

    return (param_new, new_m, new_v)