import numpy as np

def fftshiftfreqgrid(N,Fs):
    freq_res = Fs/N
    freq_grid = np.arange(N) * freq_res
    Nyq = Fs/2
    half_res = freq_res/2
    if N % 2: # odd
        pass
        # idx = 1:(N-1)/2;
        # halfpts = (N+1)/2;
        # freq_grid(halfpts) = Nyq-half_res;
        # freq_grid(halfpts+1) = Nyq+half_res;
    else:
        idx = np.arange(N//2)
        hafpts = N//2
        freq_grid[hafpts] = Nyq
    freq_grid = np.fft.fftshift(freq_grid)
    freq_grid[idx] = freq_grid[idx]-Fs
    return freq_grid