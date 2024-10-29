import os
from voice_synthesizer.analise_audio import AnalisadorAudio
from voice_synthesizer.geracao_voz import SintetizadorVoz
from voice_synthesizer.configuracao_sintese import ConfiguracaoSintese

# Configuração da síntese de voz
config = ConfiguracaoSintese(velocidade=150, volume=1.0)
sintetizador = SintetizadorVoz(config)

# Diretório dos arquivos de áudio
diretorio_audio = 'caminho/para/seus/arquivos_audio'

# Analisador de áudio
analisador = AnalisadorAudio(diretorio_audio)
caracteristicas = analisador.analisar_arquivos()
media_caracteristicas = analisador.obter_caracteristicas_media(caracteristicas)

print("Características médias:", media_caracteristicas)

# Sintetizando uma frase
texto = "Olá, bem-vindo à biblioteca Voice Synthesizer!"
sintetizador.sintetizar(texto)