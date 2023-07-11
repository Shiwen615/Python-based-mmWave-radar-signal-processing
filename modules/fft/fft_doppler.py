import numpy as np
def fft_doppler(Xcube, fft_Vel, Is_Windowed):
    # Nr = Xcube.shape[0]  # length of Chirp
    # Ne = Xcube.shape[1]  # number of receiver
    Nd = Xcube.shape[2]  # number of chirp loop

    # DopData = np.zeros((Nr, Ne, fft_Vel), dtype=np.complex128)

    # # Second fft on dopper dimension
    # for i in range(Ne):
    #     for j in range(Nr):
    #         if Is_Windowed:
    #             win_dop = np.reshape(Xcube[j, i, :], (Nd)) * np.hanning(Nd)
    #         else:
    #             win_dop = np.reshape(Xcube[j, i, :], (Nd))

    #         DopData[j, i, :] = np.fft.fftshift(np.fft.fft(win_dop, fft_Vel))
    # parallel
    if Is_Windowed:
        win_dop = Xcube * np.reshape(np.hanning(Nd), (1,1,-1))
    else:
        win_dop = Xcube
    DopData = np.fft.fftshift(np.fft.fft(win_dop, fft_Vel, axis=2), axes=2)

    return DopData
