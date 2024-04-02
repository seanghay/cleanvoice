## CleanVoice

A Fast Speech Enhancement toolkit using [Conv-TasNet (Yi Luo, Nima Mesgarani)](https://arxiv.org/abs/1809.07454)

> Only works with 16kHz audio.

## Install

```shell
pip install cleanvoice
```

## Usage


Audio file

```python
from cleanvoice import cleanvoice
from scipy.io.wavfile import write as write_wav

audio_data = cleanvoice("audio.wav")
write_wav("audio-cleaned.wav", 16000, audio_data)
```

NumPy Array as input

```python
from cleanvoice import cleanvoice
from scipy.io.wavfile import write as write_wav
import librosa

y, _ = librosa.load("audio.wav", mono=True, sr=16000)
audio_data = cleanvoice(y)
write_wav("audio-cleaned.wav", 16000, audio_data)
```

## License

`Apache-2.0`