import numpy as np
def fft_range(Xcube,fft_Rang,Is_Windowed):
    Nr = Xcube.shape[0]  # length of Chirp (number of samples)
    # Ne = Xcube.shape[1]  # number of receiver
    # Nd = Xcube.shape[2]  # length of chirp loop

    # Rangedata = np.zeros((fft_Rang, Ne, Nd), dtype=np.complex128)

    # for i in range(Ne):
    #     for j in range(Nd):
    #         if Is_Windowed:
    #             win_rng = Xcube[:, i, j] * np.hanning(Nr)
    #         else:
    #             win_rng = Xcube[:, i, j]

    #         Rangedata[:, i, j] = np.fft.fft(win_rng, fft_Rang)

    # parallel
    win_rng = Xcube* np.reshape(np.hanning(Nr), (-1,1,1))
    Rangedata = np.fft.fft(win_rng, fft_Rang, axis=0)
    return Rangedata