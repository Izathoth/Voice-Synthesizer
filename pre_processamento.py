import librosa

class PreProcessadorAudio:
    def __init__(self, caminho):
        self.caminho = caminho

    def normalizar(self):
        y, sr = librosa.load(self.caminho, sr=None)
        return librosa.util.normalize(y)