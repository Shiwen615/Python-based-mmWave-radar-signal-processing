import numpy as np
def readDCA1000(folder_locaion, numADCSamples):
    numADCBits = 16
    numRX = 4
    umLanes = 2
    max_numChirps = 459000
    isReal = 0

    with open(folder_locaion, 'rb') as bin:
        data = bin.read()
    adcData = np.frombuffer(data, dtype=np.int16)

    if numADCBits != 16:
        pass

    fileSize = adcData.size
    if isReal:
        pass
    else:
        numChirps = fileSize//2//numADCSamples//numRX
        LVDS = np.zeros((1, fileSize//2), dtype=np.complex128)
        #combine real and imaginary part into complex data
        #read in file: 2I is followed by 2Q
        # counter = 0
        # for i in range(0, fileSize, 4):
        # # for i in range(0, 20, 4):
        #     LVDS[0,counter] = adcData[i] + 1j*adcData[i+2]
        #     LVDS[0,counter+1] = adcData[i+1] + 1j*adcData[i+3]
        #     counter += 2

        # parallel
        LVDS[0, ::2] = adcData[::4]+ 1j*adcData[2::4]
        LVDS[0, 1::2] = adcData[1::4]+ 1j*adcData[3::4]

    LVDS = LVDS.reshape(numADCSamples*numRX, numChirps)

    adcData = np.zeros((numRX,numChirps*numADCSamples), dtype=np.complex128)
    if numChirps <= max_numChirps:
        for row in range(numRX):
            for i in range(numChirps):
                adcData[row, i*numADCSamples:(i+1)*numADCSamples] = LVDS[row*numADCSamples:(row+1)*numADCSamples, i]
    return adcData


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    data = readDCA1000('/home/ray/Desktop/mmWave-radar-signal-processing-and-microDoppler-classification/template data/bin_data/adc_data_0.bin',
                128)
    fig = plt.figure()
    plt.plot(np.transpose(data[:,:1000]))
    plt.legend([f"Rx_{i}" for i in range(4)])
    plt.savefig(f'/home/ray/Desktop/adcData.png')
    plt.close(fig)