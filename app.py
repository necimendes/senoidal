import streamlit as st
import os
import time
# Importe o processor corretamente, assumindo que esta na pasta src
from src.processor import load_audio, generate_waveform_image 

# --- CONFIGURAÇÕES E ESTILIZAÇÃO CSS ---

# Funcao para injetar CSS customizado (para estetica minimalista e clean)
def inject_custom_css():
    st.markdown("""
        <style>
        /* 1. Esconde elementos padrao do Streamlit (sidebar menu e rodapé) */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* 2. Estilo do container principal e títulos */
        .stContainer {
            padding-top: 2rem;
        }
        h1 {
            color: #333333; /* Cinza escuro para um look profissional */
            font-size: 2.5em;
            text-align: center;
        }
        .css-10trblm { /* Centraliza o markdown/texto principal */
            text-align: center;
        }
        
        /* 3. Estilo dos botoes para Black & White */
        .stButton>button {
            border: 2px solid #000000;
            color: #000000;
            background-color: #FFFFFF;
            padding: 0.5em 1em;
            transition: all 0.2s;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #F0F0F0;
        }
        </style>
        """, unsafe_allow_html=True)

# --- Constantes ---
OUTPUT_DIR = "generated_images" 
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
        # CHAMA O CORE LOGIC
        with st.spinner("Analisando o sinal de áudio e gerando o gráfico..."):
            y_signal, sr_rate = load_audio(temp_path)
            generate_waveform_image(y_signal, sr_rate, output_image_path)
        
        st.success("Onda sonora gerada com sucesso! ✨ A alta resolução é ideal para tatuagem.")

        # 4. EXIBE A IMAGEM E OPCAO DE DOWNLOAD
        st.subheader("Sua Arte para Tatuagem")
        st.image(output_image_path, caption='Arte final em PNG (Alta Resolução)', use_container_width=True)
        
        # Botao de download
        with open(output_image_path, "rb") as file:
            st.download_button(
                label="⬇️ Baixar Imagem (PNG)",
                data=file,
                file_name=unique_filename,
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Ocorreu um erro no processamento: {e}")
        st.warning("Verifique se o arquivo é um formato de áudio válido (.mp3, .wav) e tente novamente.")

    finally:
        # 5. LIMPEZA
        if os.path.exists(temp_path):
            os.remove(temp_path)
            try:
                os.rmdir(os.path.dirname(temp_path))
            except OSError:
                pass # Ignora se o diretorio nao estiver vazio

# --- Layout Principal da Aplicação ---

# 1. Injeta o CSS
inject_custom_css()

# 2. Configura a página
st.set_page_config(
    page_title="Soundwave Tattoo Generator",
    layout="centered",
    initial_sidebar_state="auto"
)

# 3. Cabeçalho
st.title("🌊 Soundwave Art Generator")
st.markdown("### Transforme sua música favorita em uma arte digital minimalista para tatuagem.")

st.markdown("---")

# 4. Container de Input (Melhora a UX)
with st.container(border=True):
    st.markdown("**1. Carregue seu Áudio**")
    uploaded_file = st.file_uploader(
        "Selecione um arquivo de áudio para iniciar o processamento (Max 1 minuto):", 
        type=['mp3', 'wav'], 
        label_visibility="collapsed"
    )

# 5. Lógica de Processamento
if uploaded_file is not None:
    # Mostra detalhes do arquivo
    st.info(f"Arquivo carregado: **{uploaded_file.name}** | Tamanho: {round(uploaded_file.size / 1024 / 1024, 2)} MB")
    
    # Botao para iniciar
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("GERAR ARTE DA ONDA SONORA", use_container_width=True):
            process_and_display_waveform(uploaded_file)
            
# --- Footer ---
st.markdown("---")
st.markdown("Desenvolvido por Neci Mendes | Projeto de Portfólio em Ciência da Computação")