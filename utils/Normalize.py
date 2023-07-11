import numpy as np
def Normalize(Xcube, max_val):
    Xcube = Xcube / max_val
    Angdata = Xcube.astype(np.float32)
    return Angdata