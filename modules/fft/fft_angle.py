import numpy as np
from scipy.signal import windows

def fft_angle(Xcube, fft_Ang, Is_Windowed):
    # Nr = Xcube.shape[0]  # length of Chirp
    Ne = Xcube.shape[1]  # length of receiver
    # Nd = Xcube.shape[2]  # length of chirp loop

    # AngData = np.zeros((Nr, fft_Ang, Nd), dtype=np.complex128)
    # for i in range(Nd):
    #     for j in range(Nr):
    #         if Is_Windowed:
    #             win_xcube = np.reshape(Xcube[j, :, i], (Ne)) * windows.taylor(Ne)
    #         else:
    #             win_xcube = np.reshape(Xcube[j, :, i], (Ne)) * 1

    #         AngData[j, :, i] = np.fft.fftshift(np.fft.fft(win_xcube, axis=0, n=fft_Ang))
    # parallel
    win_xcube = Xcube * np.reshape(windows.taylor(Ne), (1,-1,1))
    AngData = np.fft.fftshift(np.fft.fft(win_xcube, axis=1, n=fft_Ang), axes=1)


    return AngData
