import scipy.constants as constant
import numpy as np
from modules.fft.fftshiftfreqgrid import fftshiftfreqgrid

class GetParamsValue():
    def __init__(self) -> None:
        # constant parameters
        self.c = constant.c
        self.fc = 77e9
        self._lambda = self.c/self.fc
        self.Rx = 4
        self.Tx = 2

        # configuration parameters
        self.Fs = 4*10**6
        self.sweepSlope = 21.0017e12
        self.samples = 128
        self.loop = 255


        self.Tc = 120e-6
        self.fft_Rang = 134
        self.fft_Vel = 256
        self.fft_Ang = 128
        self.num_crop = 3
        self.max_value = 1e+04

        # Creat grid table
        freq_res = self.Fs/self.fft_Rang
        freq_grid = np.arange(self.fft_Rang) * freq_res
        self.rng_grid = freq_grid*self.c/self.sweepSlope/2 # d=frediff_grid*c/sweepSlope/2;\n',

        w = np.linspace(-1,1,self.fft_Ang) # angle_grid\n',
        self.agl_grid = np.arcsin(w)*180/np.pi # [-1,1]->[-pi/2,pi/2]\n',

        # velocity_grid
        dop_grid = fftshiftfreqgrid(self.fft_Vel,1/self.Tc) # now fs is equal to 1/Tc\n',
        self.vel_grid = dop_grid*self._lambda/2;   # unit: m/s, v = lamda/4*[-fs,fs], dopgrid = [-fs/2,fs/2]\n',

if __name__ == "__main__":
    data = GetParamsValue()
    print(data.rng_grid.shape)
    print(data.agl_grid.shape)
    print(data.vel_grid.shape)