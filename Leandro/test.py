import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.io import wavfile

with open('debug.txt') as data:
    y = data.readlines()
    y = [float(i) for i in y]

t = np.arange(0, len(y))/44100
y = np.array(y, dtype=np.float32)
wavfile.write('pirates_clarinete.wav', 44100, y)
plt.plot(y)
plt.show()