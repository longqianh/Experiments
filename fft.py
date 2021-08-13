''' 
Fourier Transform Experiments

'''

import numpy as np

fs = 100
T = 10
t = np.linspace(0, T, int(T * fs))
a = np.sin(t)
a_hat = np.fft.fft(a)

# d=采样间隔，这里是每1/fs采一次样
freq = np.fft.fftfreq(10, d=1 / fs)
print(freq)
