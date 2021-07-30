# english_asr_pip_wheel
A pip wheel for custom AI model
[English-ASR pip wheel](https://pypi.org/project/english-asr/1.1/)

## Installation
- tensorflow
- numpy
- librosa

## Models
- [Conformer Transducer](https://arxiv.org/abs/2005.08100) using [LibriSpeech](http://www.openslr.org/12) dataset.

## How To Run
```
from english_asr.conformer import get_text_from_speech
out = get_text_from_speech('audio.wav')
```


