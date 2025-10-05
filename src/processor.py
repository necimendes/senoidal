import librosa
import librosa.display
import matplotlib.pyplot as plt
import os
import numpy as np # adicionado para manipulação de array

def load_audio(file_path: str):
    """
    carrega o áudio de um arquivo local (.mp3 ou .wav) e retorna o sinal de amplitude (y)
    e a taxa de amostragem (sr).

    :param file_path: caminho local do arquivo de áudio.
    :return: uma tupla (y, sr) contendo o array do sinal e a taxa de amostragem.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    try:
        # carrega o áudio. sr=none mantém a taxa de amostragem original do arquivo.
        y, sr = librosa.load(file_path, sr=None)
        print(f"Áudio carregado com sucesso. SR: {sr} Hz, Duração: {len(y)/sr:.2f} segundos.")
        return y, sr
    except Exception as e:
        # captura erros comuns de formato ou corrupção
        print(f"Erro ao carregar o áudio com librosa: {e}")
        raise

def generate_waveform_image(y_signal: np.ndarray, sr_rate: int, output_path: str, dpi: int = 600):
    """
    gera e salva a imagem da forma de onda sonora em alta resolução (black and white).

    :param y_signal: array do sinal de amplitude.
    :param sr_rate: taxa de amostragem.
    :param output_path: caminho para salvar a imagem (.png).
    :param dpi: resolução da imagem (dots per inch) - 600 ou mais para tatuagem.
    """
    plt.figure(figsize=(10, 4)) # define o tamanho da figura (proporcionalmente bom)

    # gera a visualização da forma de onda
    librosa.display.waveshow(
        y_signal, 
        sr=sr_rate, 
        color='black', 
        alpha=0.8 # define a cor e a opacidade
    )

    plt.axis('off') # remove os eixos (x e y), títulos, e bordas
    plt.margins(0, 0) # remove margens extras ao redor do gráfico
    plt.gca().xaxis.set_major_locator(plt.NullLocator()) # garante que nada de eixo X apareça
    plt.gca().yaxis.set_major_locator(plt.NullLocator()) # garante que nada de eixo Y apareça

    # salva a figura com alta resolução
    plt.savefig(
        output_path, 
        bbox_inches='tight', # corta espaços em branco desnecessários
        pad_inches=0,        # garante que o corte seja rente
        transparent=True,    # fundo transparente, ideal para tatuagem
        dpi=dpi              # alta resolução
    )
    plt.close() # fecha a figura para liberar memória

# campo de teste

if __name__ == '__main__':
    TEST_FILE_NAME = "sof.mp3" 
    OUTPUT_IMAGE_NAME = "waveform_output.png"

    try:
        # 1. carrega o áudio
        y_signal, sr_rate = load_audio(TEST_FILE_NAME) 

        # 2. gera a imagem da onda sonora
        generate_waveform_image(y_signal, sr_rate, OUTPUT_IMAGE_NAME)

        print(f"\nImagem gerada com SUCESSO! Verifique o arquivo '{OUTPUT_IMAGE_NAME}' na pasta raiz.")

    except FileNotFoundError:
        print(f"\nERRO: O arquivo de teste '{TEST_FILE_NAME}' não foi encontrado.")
    except Exception as e:
        print(f"\nFalha no teste: {e}")