## Librosa-Drum-Point
这又是一个新的项目，利用librosa对音频进行修改。
什么？你问我librosa是什么？去这里看→[https://librosa.github.io/librosa/](https://librosa.github.io/librosa/)
打开cmd或者Powershell（一定要以管理员身份运行！没有UAC的当我没说）
输入以下指令安装依赖库：

```powershell
conda install -c conda-forge librosa && conda install -c conda-forge ffmpeg
```

然后我们就可以开始使用这些库了，当然首先要导入：

```python
import librosa
import librosa.display
```

为什么不导入ffmpeg？因为它是个解码库呀！

如何对鼓点进行切分呢？这里使用的样本文件是drum.wav

首先要先加载这个文件，利用

```python
audio_path = 'drum.wav'
y,sr=librosa.load(audio_path)
```

然后就要计算频谱，使用一下方法：

```python
D=librosa.stft(y)
db=librosa.core.amplitude_to_db(D)
librosa.display.specshow(db)
plt.show()
```

接着要计算频谱包络，把它设为一个变量

```python
energy=librosa.onset.onset_strength(y,sr)
```

根据频谱包络，检测鼓点并以帧的形式保存

```python
events=librosa.onset.onset_detect(y,sr)
```

利用 librosa.onset.onset_backtrack 根据鼓点的峰值时间点, 往回查找峰起始帧

```python
frames=librosa.onset.onset_backtrack(events,energy)
```

然后利用 librosa.core.frames_to_samples(slice_frames) 将帧转化为样本点

```python
points=librosa.core.frames_to_samples(frames) 
```

最后我们要进行切片，首先要创建文件保存的目录

```python
import os #导入系统命令库
if not os.path.exists('./Drum-Point-Cutting'):
    os.mkdir('./Drum-Point-Cutting')
```

然后取得数据：

```python
num_points = len(y) # 音频总取样点数
num_slice_points = len(points) # 切片点数
```

进行切片操作：

```python
for i in range(num_slice_points):
    # code 7
    librosa.core.frames_to_samples(frames)
    filepath='./Drum-Point-Cutting/drum'+str(i)+'.wav'
    if i==(num_slice_points-1):
        break
  librosa.output.write_wav(filepath,y[points[i]:points[i+1]],sr,norm=0)
```

因为当i等于序列中最大值的时候，i+1就会爆炸，所以这里需要一个if做判断，如果i已经到了最大值，那么就break出循环，这样才不会爆炸^_^

这样，我们就把文件导出到了Durm-Point-Cutting目录下（我这里已经把文件夹名字改为了Drum-Points

利用这种方式可以对文件中的鼓点进行切片，就可以去掉不必要的片段了。

###### （要是丢一首歌进去会怎么样呢？？？）

