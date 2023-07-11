from read_data.readDCA1000 import readDCA1000

samples = 128# num of samples per chirp
loop = 255
Tx = 2


folder_location = '/home/ray/Desktop/mmWave-radar-signal-processing-and-microDoppler-classification/template data/bin_data/adc_data_0.bin'
data = readDCA1000(folder_location, samples)
data_length = data.shape[1]
data_each_frame = samples*loop*Tx
Frame_num = data_length/data_each_frame

if __name__ == '__main__':
    print(data.shape)