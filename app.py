import streamlit as st
import os
import time
from src.processor import load_audio, generate_waveform_image

# --- Configurações da Página ---
st.set_page_config(
    page_title="Soundwave Tattoo Generator",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Constantes ---
OUTPUT_DIR = "generated_images" # Diretorio para salvar as imagens
os.makedirs(OUTPUT_DIR, exist_ok=True)


# --- Funções de Processamento no Streamlit ---

def process_and_display_waveform(uploaded_file):
    """Lida com o processamento do arquivo de audio e exibe a imagem no Streamlit."""
    
    # 1. Salva o arquivo temporariamente no disco para que o librosa possa ler
    temp_path = os.path.join("temp_uploaded_audio", uploaded_file.name)
    os.makedirs(os.path.dirname(temp_path), exist_ok=True)
    
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Define o caminho de saida da imagem
    unique_filename = f"waveform_{int(time.time())}.png"
    output_image_path = os.path.join(OUTPUT_DIR, unique_filename)

    try:
        # 2. CHAMA O CORE LOGIC (Processamento da Fase 1)
        st.info("Processando áudio e gerando o gráfico de onda...")
        y_signal, sr_rate = load_audio(temp_path)
        
        # 3. GERA A IMAGEM
        generate_waveform_image(y_signal, sr_rate, output_image_path)
        
        st.success("Onda sonora gerada com sucesso! ✨")

        # 4. EXIBE A IMAGEM E OPCAO DE DOWNLOAD
        st.subheader("Sua Arte para Tatuagem")
        st.image(output_image_path, caption='Sua Onda Sonora em Alta Resolução', use_column_width=True)
        
        # Botao de download
        with open(output_image_path, "rb") as file:
            st.download_button(
                label="Baixar Imagem (Alta Resolução PNG)",
                data=file,
                file_name=unique_filename,
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Ocorreu um erro no processamento: {e}")
        st.warning("Certifique-se de que o arquivo é um formato de áudio válido (.mp3, .wav) e que não está corrompido.")

    finally:
        # 5. LIMPEZA: Remove o arquivo temporario
        if os.path.exists(temp_path):
            os.remove(temp_path)
            os.rmdir(os.path.dirname(temp_path)) # Tenta remover o diretorio temporario

# --- Layout do Streamlit ---

st.title("🌊 Soundwave Tattoo Generator")
st.markdown("Transforme a sua música favorita em uma arte minimalista para tatuagem.")

# Area de upload de arquivos
uploaded_file = st.file_uploader(
    "1. Faça o upload do seu arquivo de áudio:", 
    type=['mp3', 'wav'], 
    help="Arquivos muito longos (>1 minuto) podem demorar para processar."
)

if uploaded_file is not None:
    # Mostra informacoes do arquivo
    st.markdown(f"**Arquivo:** `{uploaded_file.name}`")
    st.markdown(f"**Tamanho:** `{round(uploaded_file.size / 1024 / 1024, 2)} MB`")
    
    # Botao de processamento
    if st.button("2. Gerar Onda Sonora"):
        process_and_display_waveform(uploaded_file)

# --- Footer ---
st.markdown("---")
st.markdown(f"Desenvolvido por Neci Mendes | {os.getenv('APP_VERSION', 'v1.0.0')}")