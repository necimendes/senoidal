import unittest
import os
import numpy as np
from unittest.mock import patch
from src.processor import load_audio, generate_waveform_image

# --- configuracao de mocks ---
# dados simulados (sAmplitude 'y' e sample rate 'sr') que
# o librosa.load do teste ira retornar, garantindo que o teste nao dependa de um arquivo real.
MOCK_SR = 22050
# array numpy simulado de amplitudes (tamanho 50)
MOCK_Y = np.array([0.1, 0.2, 0.0, -0.1, -0.2] * 10, dtype=np.float32)

class TestAudioProcessor(unittest.TestCase):

    def setUp(self):
        """prepara o ambiente e define nomes de arquivos temporários antes de cada teste."""
        self.input_file = "test_input.mp3"
        self.output_image = "test_output.png"

        # simula a criacao de um arquivo local para os testes de leitura
        with open(self.input_file, 'w') as f:
            f.write("mock_audio_data")

    def tearDown(self):
        """limpa arquivos temporários criados apos cada teste."""
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_image):
            os.remove(self.output_image)

    # teste load_audio
    
    @patch('librosa.load', return_value=(MOCK_Y, MOCK_SR))
    def test_load_audio_success(self, mock_load):
        """verifica se o carregamento do audio retorna os dados e sr esperados."""
        y, sr = load_audio(self.input_file)
        
        # 1. verifica a taxa de amostragem
        self.assertEqual(sr, MOCK_SR)
        
        # 2. verifica o formato e tamanho do sinal
        self.assertTrue(isinstance(y, np.ndarray))
        self.assertEqual(len(y), len(MOCK_Y))

    def test_load_audio_file_not_found(self):
        """verifica se levanta o erro filenotfounderror para arquivos inexistentes."""
        with self.assertRaises(FileNotFoundError):
            load_audio("arquivo_que_nao_existe.mp3")

    # teste generate_waveform_image
    
    @patch('matplotlib.pyplot.savefig')
    def test_generate_waveform_image_called(self, mock_savefig):
        """verifica se a funcao de salvar imagem é chamada com os parametros corretos de alta resolucao."""
        
        generate_waveform_image(MOCK_Y, MOCK_SR, self.output_image)
        
        # verifica se o matplotlib.pyplot.savefig foi chamado
        mock_savefig.assert_called_once()
        
        # verifica os argumentos de salvamento (garantindo que o DPI e o 'tight' estao corretos)
        mock_savefig.assert_called_with(
            self.output_image,
            bbox_inches='tight',
            pad_inches=0,
            transparent=True,
            dpi=600
        )
    
    def test_generate_waveform_image_creates_file(self):
        """testa se a funcao realmente cria um arquivo no disco (sem mock de savefig)."""
        # limpamos o arquivo de output antes de rodar
        if os.path.exists(self.output_image):
            os.remove(self.output_image)
            
        generate_waveform_image(MOCK_Y, MOCK_SR, self.output_image)
        
        # verifica se o arquivo foi criado
        self.assertTrue(os.path.exists(self.output_image))


if __name__ == '__main__':
    unittest.main()