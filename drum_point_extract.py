from __future__ import print_function

import os

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
audio_path = 'drum.wav'
# code 1
y,sr=librosa.load(audio_path)
# code 2
D=librosa.stft(y)
db=librosa.core.amplitude_to_db(D)
librosa.display.specshow(db)
#plt.show()
# code 3
energy=librosa.onset.onset_strength(y,sr)
# 绘制包络
plt.plot(librosa.onset.onset_strength(y,sr),color='c')
#plt.show()
# code 4
events=librosa.onset.onset_detect(y,sr)
#print(energy)
# code 5
frames=librosa.onset.onset_backtrack(events,energy)
#print(frames)
# code 6
points=librosa.core.frames_to_samples(frames) 
#print(points)
if not os.path.exists('./Drum-Point-Cutting'):
    os.mkdir('./Drum-Point-Cutting')
num_points = len(y) # 音频总取样点数
num_slice_points = len(points) # 切片点数

for i in range(num_slice_points):
    # code 7
    librosa.core.frames_to_samples(frames)
    filepath='./Drum-Point-Cutting/drum'+str(i)+'.wav'
    if i==(num_slice_points-1):
        break
    librosa.output.write_wav(filepath,y[points[i]:points[i+1]],sr,norm=0)