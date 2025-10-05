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
    
    # ... (código da função load_audio) ...

# --- Teste Rápido (para uso local) ---
if __name__ == '__main__':
    # Use o nome exato do arquivo que você copiou para a raiz
    TEST_FILE_NAME = "sof.mp3" 

    try:
        # 1. Tenta carregar o áudio.
        y_signal, sr_rate = load_audio(TEST_FILE_NAME) 

        # 2. Se for bem-sucedido, imprime os resultados.
        print("\n--- Resultados do Teste ---")
        print(f"Sinal de Amostras (Array 'y') - Tipo: {type(y_signal)}")
        print(f"Primeiros 10 valores (Amplitudes): {y_signal[:10]}")
        print(f"Taxa de Amostragem (SR): {sr_rate} Hz")
        print(f"Teste de carregamento concluído com SUCESSO! ✅")

    except FileNotFoundError:
        print(f"\nERRO: O arquivo de teste '{TEST_FILE_NAME}' não foi encontrado na pasta raiz.")
        print("Verifique se o nome do arquivo no código é o mesmo do arquivo copiado.")
    except Exception as e:
        print(f"\nFalha no teste de carregamento de áudio: {e} ❌")