import librosa
import os

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