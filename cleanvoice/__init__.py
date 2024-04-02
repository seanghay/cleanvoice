import onnxruntime as rt
import numpy as np
import os
import librosa
from typing import Union

MODEL_PATH = os.path.join(os.path.dirname(__file__), "convtasnet.onnx")

sess_options = rt.SessionOptions()
sess_options.graph_optimization_level = rt.GraphOptimizationLevel.ORT_DISABLE_ALL

MODEL = rt.InferenceSession(MODEL_PATH, sess_options=sess_options)


def audio_float_to_int16(
  audio: np.ndarray, max_wav_value: float = 32767.0
) -> np.ndarray:
  """Normalize audio and convert to int16 range"""
  audio_norm = audio * (max_wav_value / max(0.01, np.max(np.abs(audio))))
  audio_norm = np.clip(audio_norm, -max_wav_value, max_wav_value)
  audio_norm = audio_norm.astype("int16")
  return audio_norm


def cleanvoice(audio: Union[str, np.ndarray]) -> np.ndarray:
  """
  Return clean speech audio. (It only accepts 16kHz Mono audio.)

  Parameters:
      audio (Union[str, np.ndarray]): Input audio as either a filepath to an audio file or a NumPy array.

  Returns:
      np.ndarray: Cleaned 16-Bit Integer audio as a NumPy array.
  """
  y = None

  # audio must be resampled to 16kHz
  if isinstance(audio, np.ndarray):
    y = audio

  if isinstance(audio, str):
    y, _ = librosa.load(audio, sr=16000, mono=True)

  if y is None:
    raise "input audio is invalid"

  waveform = np.expand_dims(np.expand_dims(y, axis=0), axis=0)
  results = MODEL.run(None, {"input": waveform})
  return audio_float_to_int16(results[0].squeeze())
