# Voice Synthesizer

**A biblioteca Voice Synthesizer é uma ferramenta em Python para análise de áudio e síntese de voz. Ela permite que você analise arquivos de áudio, extraia características, treine modelos de voz e sintetize voz a partir de texto. É ideal para aplicações de processamento de áudio e assistentes virtuais.**

## Instalação

**Para utilizar a biblioteca, você precisa ter o Python instalado em sua máquina. Você também precisará instalar as seguintes dependências:**
```
pip install numpy librosa pyttsx3 scikit-learn
```

## Estrutura da Biblioteca

**A biblioteca contém os seguintes módulos:**

```analise_audio.py:``` Para análise de arquivos de áudio.

```geracao_voz.py:``` Para sintetizar voz a partir de texto.

```treinamento_modelo.py:``` Para treinar modelos de voz.

```configuracao_sintese.py:``` Para configurar parâmetros de síntese de voz.

```pre_processamento.py:``` Para normalizar arquivos de áudio.     

```extracao_caracteristicas.py:``` Extrai características da voz dos arquivos.

# Exemplo de Uso

**Abaixo está um exemplo de como usar a biblioteca para analisar arquivos de áudio e sintetizar voz:**
```
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
```

## Funcionalidades

**Análise de Áudio: Extração de características de arquivos de áudio (MFCC, pitch e energia).**

**Síntese de Voz: Conversão de texto em fala com configurações de velocidade e volume.**

**Treinamento de Modelo: Treinamento de um modelo de aprendizado de máquina para gerar áudio a partir de características.**

**Pré-processamento: Normalização de arquivos de áudio.**


## Contribuições

**Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.**

# Licença

**Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.**


# Avisos:

**É necessário criar um diretório contendo os arquivos de áudio no formato .mp3 que você deseja analisar e utilizar na síntese de voz. Para obter resultados mais eficazes e variados, é altamente recomendado que você tenha, no mínimo, 30 arquivos de voz diferentes nesse diretório. Isso garantirá uma melhor análise das características de áudio e uma síntese de voz mais natural e diversificada.**



# Aviso Legal: 
**Esta biblioteca é destinada apenas para fins legais e éticos. A utilização de arquivos de áudio deve respeitar todos os direitos autorais e leis de propriedade intelectual. É responsabilidade do usuário garantir que possui a permissão necessária para utilizar qualquer conteúdo de áudio processado com esta biblioteca.**

