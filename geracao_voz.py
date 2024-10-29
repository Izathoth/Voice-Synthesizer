import pyttsx3

class SintetizadorVoz:
    def __init__(self, config):
        self.engine = pyttsx3.init()
        self.configurar_voz(config)

    def configurar_voz(self, config):
        self.engine.setProperty('rate', config.velocidade)
        self.engine.setProperty('volume', config.volume)
        if config.id_voz:
            self.engine.setProperty('voice', config.id_voz)

    def sintetizar(self, texto):
        self.engine.say(texto)
        self.engine.runAndWait()