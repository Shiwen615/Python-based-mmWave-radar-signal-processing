import numpy as np

def hanning(n):
    ret = np.arange(1,n+1)
    return .5 * (1-np.cos(2*np.pi*ret/(n+1)))