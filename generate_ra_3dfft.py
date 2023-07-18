from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from config.get_params_value import GetParamsValue
from modules.fft.test import *
from utils.Normalize import Normalize

params = GetParamsValue()

c = params.c # Speed of light in air (m/s)
fc = params.fc # Center frequency (Hz)
_lambda = params._lambda
Rx = params.Rx
Tx = params.Tx

# configuration parameters
Fs = params.Fs
sweepSlope = params.sweepSlope
samples = params.samples
loop = params.loop

Tc = params.Tc # us
fft_Rang = params.fft_Rang
fft_Vel = params.fft_Vel
fft_Ang = params.fft_Ang
num_crop = params.num_crop
max_value = params.max_value # normalization the maximum of data WITH 1843

# Creat grid table
rng_grid = params.rng_grid
agl_grid = params.agl_grid
vel_grid = params.vel_grid

# Algorithm parameters
data_each_frame = samples*loop*Tx
set_frame_number = 30
frame_start = 1
frame_end = set_frame_number
Is_Windowed = 1# 1==> Windowing before doing range and angle fft
Is_plot_rangeDop = 1

load_mat = loadmat('/home/ray/Desktop/mmWave-radar-signal-processing-and-microDoppler-classification/template data/bms1000_30fs.mat')
# test_mat = loadmat('/home/ray/Desktop/mmWave-radar-signal-processing-and-microDoppler-classification/template data/cms1000_30fs.mat')
# test_mat = loadmat('/home/ray/Desktop/mmWave-radar-signal-processing-and-microDoppler-classification/template data/pms1000_30fs.mat')
data_frames = load_mat['data_frames']

# for i in range(set_frame_number):
i = 0

data_frame = data_frames[:, i*data_each_frame:(i+1)*data_each_frame]
# for cj in range(Tx*loop):
#     temp_data = data_frame[:, cj*samples:(cj+1)*samples]
#     data_chirp[:,:,cj] = temp_data

# parallel
data_chirp = np.transpose(np.reshape(data_frame, (Rx, -1, samples)), (0,2,1))

chirp_odd = data_chirp[:, :, ::2]
chirp_even = data_chirp[:, :, 1::2]

# Range FFT for odd chirps
chirp_odd = np.transpose(chirp_odd, (1, 0, 2))
chirp_even = np.transpose(chirp_even, (1, 0, 2))

# Range FFT for odd chirps
Rangedata_odd = fft_range(chirp_odd,fft_Rang,Is_Windowed)
# Range FFT for even chirps
Rangedata_even = fft_range(chirp_even,fft_Rang,Is_Windowed)

#Doppler FFT
# Dopplerdata_odd = fft_doppler(Rangedata_odd, fft_Vel, False)
# Dopplerdata_even = fft_doppler(Rangedata_even, fft_Vel, False)
# Dopdata_sum = np.squeeze(np.mean(np.abs(Dopplerdata_odd), axis=1))

Rangedata_merge = np.concatenate((Rangedata_odd, Rangedata_even), axis=1)
# Angle FFt
Angdata = fft_angle(Rangedata_merge,fft_Ang,Is_Windowed)
Angdata_crop = Angdata[num_crop:fft_Rang - num_crop, :, :]
Angdata_crop = Normalize(Angdata_crop, max_value)

Xpow = np.abs(Angdata_crop)
Xpow = np.squeeze(np.sum(Xpow, axis=2) / Xpow.shape[2])

Xsnr = Xpow

fig = plt.figure(frameon=False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(Xsnr[::-1], aspect='auto')
plt.savefig('RF_image.png')
plt.close(fig)