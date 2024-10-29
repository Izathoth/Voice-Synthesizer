import librosa
import numpy as np

def extrair_caracteristicas(caminho):
    y, sr = librosa.load(caminho, sr=None)
    return {
        'mfccs': np.mean(librosa.feature.mfcc(y=y, sr=sr).T, axis=0),
        'pitch': np.mean(librosa.feature.pitch(y=y, sr=sr)),
        'energia': np.mean(librosa.feature.rms(y=y)),
    }