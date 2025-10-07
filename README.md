# Projeto: Soundwave Art Generator

## Visão Geral do Projeto

O **Soundwave Art Generator** é uma aplicação web construída em Python (Streamlit) para transformar qualquer arquivo de áudio (MP3 ou WAV) em uma imagem PNG de alta resolução. O objetivo principal do projeto é servir como uma ferramenta minimalista e precisa para a criação de designs de tatuagens baseadas em ondas sonoras.

Este projeto demonstra proficiência em **Processamento Digital de Sinais (DSP)**, **Visualização de Dados**, e **Desenvolvimento Web (*rapid prototyping*)**.

-----

## Motivação e Storytelling

A inspiração para o projeto surgiu do desejo de ter uma tatuagem de onda sonora, mas com um traço delicado (*fine-line*) e geometricamente preciso. A principal lacuna no mercado era a falta de controle sobre a **resolução (DPI)** e a **estilização minimalista** da onda, que muitas vezes é entregue em baixa qualidade ou com excesso de ruído visual.

O código foi desenvolvido para garantir que o *core logic* entregue a visualização mais fiel possível do sinal de áudio, com alta qualidade (600 DPI) para arte final.

-----

## O que a Onda Sonora Representa (Física e DSP)

O gráfico gerado pelo aplicativo é a **representação visual direta do Sinal de Amplitude no Domínio do Tempo** do seu arquivo de áudio.

| Conceito | Representação no Gráfico | O que significa? |
| :--- | :--- | :--- |
| **Amplitude ($\mathbf{Y}$)** | A **altura vertical** dos picos e vales. | O volume (intensidade) do som. Picos altos = som alto; Linha reta no centro = silêncio. |
| **Domínio do Tempo ($\mathbf{X}$)** | O **eixo horizontal** da esquerda para a direita. | A duração do áudio. O ponto mais à esquerda é o início do som; o ponto mais à direita é o fim. |
| **Taxa de Amostragem ($\mathbf{SR}$)** | A **densidade** de pontos no gráfico. | Quantos "pedaços" de áudio são medidos por segundo (geralmente 44100 Hz). É crucial para a fidelidade da onda. |

-----

## Stack Tecnológico

| Categoria | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.x | Lógica central e Web Framework. |
| **Processamento Digital de Sinais (DSP)** | **`Librosa`** | Análise, leitura e decodificação do áudio (WAV/MP3). |
| **Visualização** | **`Matplotlib`** | Geração do gráfico da forma de onda em alta resolução (PNG). |
| **Interface Web** | **`Streamlit`** | Criação da interface de usuário (*rapid prototyping*). |
| **Versionamento** | Git Flow | Gerenciamento de *branches* e histórico de desenvolvimento. |

-----

## Notas de Desenvolvimento e Versão Futura

### Tentativa de Extração de Link

A funcionalidade para extrair e cortar o áudio de *links* (ex: YouTube) foi iniciada, mas **removida** do código final para garantir a estabilidade e o *deployment* limpo. O desafio residia na dependência de ferramentas externas de sistema (**FFmpeg** e **yt-dlp**) para o processamento de áudio, o que introduzia complexidade na instalação e no *deployment*. A funcionalidade pode ser reintroduzida em uma *feature branch* futura.

### Estilização Futura (Minimalismo Extremo)

A versão atual da onda sonora é precisa e fina (utilizando `linewidth` baixo). No entanto, o objetivo final é atingir um visual ainda mais minimalista e *clean*. Isso exigirá **pesquisa e desenvolvimento (P\&D)** para:

  * Implementar uma visualização no estilo **Peak Plot (Agulha)**, que simplifica a onda, plotando apenas os picos de energia (RMS) do áudio.
  * Ajustar a densidade do gráfico sem comprometer a representação dos picos de volume.

-----

## Instalação e Execução

### Pré-requisitos

  * Python 3.8+
  * Git

### 1\. Clonar e Configurar o Ambiente

```bash
# 1. Clonar o repositório
git clone https://www.youtube.com/watch?v=RqfwLeY952s
cd [NOME-DO-PROJETO]

# 2. Criar e Ativar o Ambiente Virtual
python3 -m venv venv
source venv/Scripts/activate  # Ou '.\venv\Scripts\Activate' no Windows Prompt/PowerShell

# 3. Instalar Dependências
pip install -r requirements.txt
```

### 2\. Executar a Aplicação Web

Certifique-se de que seu ambiente `(venv)` está ativo:

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no seu navegador.

-----

## Cronograma do Projeto (Sprints)

### Fase 1: Core Logic e Processamento de Sinais (Concluída)

| Entregável | Status |
| :--- | :--- |
| **1.2** Módulo de Leitura de Arquivos (WAV/MP3) | ✅ |
| **1.3** Módulo de Geração Gráfica (Alta Resolução) | ✅ |
| **1.5** Implementação de Testes Unitários (`unittest`) | ✅ |

### Fase 2: Desenvolvimento da Interface Web (Concluída)

| Entregável | Status |
| :--- | :--- |
| **2.1** Configuração do Framework (Streamlit) | ✅ |
| **2.2/2.3** Interface de Usuário e Integração com Core Logic | ✅ |
| **2.4** Estilização e UX (Design Minimalista e Limpo) | ✅ |

### Fase 3: Documentação e Implantação (Concluída)

| Entregável | Status |
| :--- | :--- |
| **3.2** Documentação Técnica do README | ✅ |
| **3.3** Implantação do Aplicativo Web (Deployment) | ✅ |
| **3.4** Licença e Contribuição | ✅ |

-----

## Contribuição

Contribuições, sugestões e relatórios de *bugs* são bem-vindos\! Siga o fluxo **Git Flow** para novas *features* e *hotfixes*.
