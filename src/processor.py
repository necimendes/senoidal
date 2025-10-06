import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
# Removidos: subprocess, tempfile, shutil (não são mais necessários)

def load_audio(file_path: str):
    """
    Carrega o áudio de um arquivo local (.mp3 ou .wav) e retorna o sinal de amplitude (y)
    e a taxa de amostragem (sr).

    :param file_path: Caminho local do arquivo de áudio.
    :return: Uma tupla (y, sr) contendo o array do sinal e a taxa de amostragem.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    try:
        # Carrega o áudio. sr=None mantém a taxa de amostragem original do arquivo.
        y, sr = librosa.load(file_path, sr=None)
        print(f"Áudio carregado com sucesso. SR: {sr} Hz, Duração: {len(y)/sr:.2f} segundos.")
        return y, sr
    except Exception as e:
        # Captura erros comuns de formato ou corrupção
        print(f"Erro ao carregar o áudio com librosa: {e}")
        raise

def generate_waveform_image(y_signal: np.ndarray, sr_rate: int, output_path: str, dpi: int = 600):
    """
    Gera e salva a imagem da forma de onda sonora em alta resolução (black and white).

    :param y_signal: Array do sinal de amplitude.
    :param sr_rate: Taxa de amostragem.
    :param output_path: Caminho para salvar a imagem (.png).
    :param dpi: Resolução da imagem (Dots Per Inch) - 600 ou mais para tatuagem.
    """
    plt.figure(figsize=(10, 4)) # Define o tamanho da figura (proporcionalmente bom)

    # Gera a visualização da forma de onda
    librosa.display.waveshow(
        y_signal, 
        sr=sr_rate, 
        color='black', 
        alpha=0.8 # Define a cor e a opacidade
    )

    # --- Estilização Essencial para Tatuagem ---
    plt.axis('off') # Remove os eixos (x e y), títulos, e bordas
    plt.margins(0, 0) # Remove margens extras ao redor do gráfico
    plt.gca().xaxis.set_major_locator(plt.NullLocator()) # Garante que nada de eixo X apareça
    plt.gca().yaxis.set_major_locator(plt.NullLocator()) # Garante que nada de eixo Y apareça

    # Salva a figura com alta resolução
    plt.savefig(
        output_path, 
        bbox_inches='tight', # Corta espaços em branco desnecessários
        pad_inches=0,        # Garante que o corte seja rente
        transparent=True,    # Fundo transparente, ideal para tatuagem
        dpi=dpi              # Alta resolução
    )
    plt.close() # Fecha a figura para liberar memória


# ----------------------------------------------------------------------
# Bloco de Teste (ATUALIZADO PARA ARQUIVO LOCAL)
# ----------------------------------------------------------------------

if __name__ == '__main__':
    # ATENÇÃO: Coloque um arquivo de áudio (ex: 'sample.wav' ou 'test.mp3') na raiz do projeto
    TEST_FILE_NAME = "sample.wav" 
    OUTPUT_IMAGE_NAME = "waveform_local_output.png"
    
    try:
        print(f"Iniciando processamento do arquivo local: {TEST_FILE_NAME}")

        # 1. Carrega o áudio
        y_signal, sr_rate = load_audio(TEST_FILE_NAME) 
        
        # 2. Gera a imagem da onda sonora
        generate_waveform_image(y_signal, sr_rate, OUTPUT_IMAGE_NAME)
        
        print(f"\nOnda sonora do arquivo local gerada com SUCESSO! ✅ Verifique o arquivo '{OUTPUT_IMAGE_NAME}' na pasta raiz.")

    except FileNotFoundError:
        print(f"\nERRO: O arquivo de teste '{TEST_FILE_NAME}' não foi encontrado. Por favor, coloque um arquivo .wav ou .mp3 na raiz do projeto.")
    except Exception as e:
        print(f"\nFalha no teste: {e} ❌")