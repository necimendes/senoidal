# Soundwave Tattoo Generator

Este projeto visa desenvolver uma aplicação web para gerar imagens de formas de onda sonora de alta resolução, utilizáveis como base para tatuagens. A aplicação suportará o upload de arquivos e a extração de áudio via link (YouTube).

## Sprints

---

## Fase 1: Core Logic e Processamento de Sinais

**Objetivo:** Estabelecer o *back-end* principal capaz de processar o áudio e gerar a imagem de alta fidelidade.

| ID | Entregável | Status |
| :--- | :--- | :--- |
| **1.1** | **Configuração do Ambiente:** Repositório inicial configurado com `requirements.txt` e ambiente Python com bibliotecas (`librosa`, `matplotlib`, `pydub`, `yt-dlp`). | ☐ |
| **1.2** | **Módulo de Leitura de Arquivos:** Função Python robusta para carregar e decodificar arquivos de áudio nos formatos **WAV e MP3**, retornando o array de amplitude e a taxa de amostragem. | ☐ |
| **1.3** | **Módulo de Geração Gráfica:** Função principal de visualização (`plot`) utilizando `matplotlib`, configurada para **eliminar eixos** (`plt.axis('off')`), garantir fundo transparente e salvar em **alta resolução (DPI > 600)** para impressão. | ☐ |
| **1.4** | **Módulo de Extração de Link:** Implementação da lógica para receber um link (ex.: YouTube), extrair e baixar apenas o **stream de áudio** em um formato processável (ex.: temporário WAV/MP3). | ☐ |
| **1.5** | **Testes Unitários:** Verificação da precisão da onda sonora gerada e teste de *edge cases* (arquivos corrompidos ou links indisponíveis) para garantir estabilidade do *core logic*. | ☐ |

---

## Fase 2: Desenvolvimento da Interface Web (Deployment Rápido)

**Objetivo:** Criar uma interface funcional utilizando um *framework* Python para demonstrar e publicar o projeto rapidamente.

| ID | Entregável | Status |
| :--- | :--- | :--- |
| **2.1** | **Configuração do Framework:** Inicialização do projeto web utilizando **Streamlit/Flask**, criando a estrutura de rotas e o loop principal da aplicação. | ☐ |
| **2.2** | **Interface de Usuário (Upload):** Implementação dos campos de *input* no *front-end* para **upload de arquivos** (`.mp3` / `.wav`) e submissão de **links de áudio** (URL). | ☐ |
| **2.3** | **Integração Back-end/Front-end:** Conexão do formulário web com o Módulo de Geração Gráfica (Fase 1), garantindo que a imagem gerada seja renderizada na página. | ☐ |
| **2.4** | **Estilização e UX:** Aplicação de *layout* limpo e minimalista (foco em estética Black & White), garantindo uma experiência de usuário fluida e responsiva para a visualização da onda. | ☐ |
| **2.5** | **Download da Imagem:** Funcionalidade para o usuário fazer o *download* direto da imagem da onda sonora gerada em formato PNG de alta resolução. | ☐ |

---

## Fase 3: Documentação e Implantação

**Objetivo:** Finalizar o projeto para consumo público, otimizando o código e documentando o processo.

| ID | Entregável | Status |
| :--- | :--- | :--- |
| **3.1** | **Otimização e Refatoração:** Revisão do código Python (Fases 1 e 2) para melhor performance, clareza e aderência aos padrões de codificação (PEP 8). | ☐ |
| **3.2** | **Documentação Técnica:** Criação/Aperfeiçoamento do `README.md` com explicação da motivação, arquitetura técnica e detalhes sobre o **Processamento Digital de Sinais (DSP)** utilizado. | ☐ |
| **3.3** | **Deployment (Implantação):** Hospedagem do aplicativo em uma plataforma de nuvem (ex.: Heroku/Streamlit Sharing) para acesso público e demonstração. | ☐ |
| **3.4** | **Licença e Agradecimentos:** Definição da licença de código aberto (ex.: MIT) e lista de colaboradores (se houver). | ☐ |

---
