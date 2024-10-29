import os
import numpy as np
from .extracao_caracteristicas import extrair_caracteristicas

class AnalisadorAudio:
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def analisar_arquivos(self):
        return [extrair_caracteristicas(os.path.join(self.diretorio, f)) 
                for f in os.listdir(self.diretorio) if f.endswith(('.wav', '.mp3'))]

    def obter_caracteristicas_media(self, caracteristicas):
        return np.mean(caracteristicas, axis=0) if caracteristicas else None