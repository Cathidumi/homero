# homero
Solução para construção de instrumentos clínicos

Esta documentação explica o propósito do projeto, como instalá-lo, configurá-lo e utilizar a API para gerar instrumentos de pesquisa.

-----

# Homero

**Solução para construção automatizada de instrumentos clínicos e de pesquisa.**

O **Homero** é uma aplicação backend desenvolvida em Python que utiliza Inteligência Artificial Generativa (Google Gemini) para converter descrições em linguagem natural em estruturas JSON complexas de formulários de pesquisa. O sistema é capaz de interpretar solicitações de usuários e montar instrumentos completos compatíveis com padrões específicos (estrutura `StudioObject`/`SurveyItem`), incluindo lógica de navegação e metadados.

## 📋 Funcionalidades

O sistema é capaz de gerar os seguintes tipos de questões e elementos a partir de texto livre:

  * **Questões de Seleção:** `SingleSelectionQuestion` (Seleção única), `CheckboxQuestion` (Múltipla escolha).
  * **Dados Numéricos:** `IntegerQuestion` (Inteiro), `DecimalQuestion` (Decimal), `PhoneQuestion`.
  * **Dados de Texto e Data:** `TextQuestion`, `EmailQuestion`, `CalendarQuestion` (Data), `TimeQuestion` (Hora).
  * **Elementos Especiais:** `AutocompleteQuestion`, `FileUploadQuestion`.
  * **Itens Estáticos:** `TextItem` (Texto informativo), `ImageItem` (Imagens).
  * **Estrutura e Navegação:** Gera automaticamente a árvore de navegação (`navigationList`) e o container de itens (`itemContainer`), vinculando nós de início e fim.

## 🚀 Tecnologias Utilizadas

  * [Python 3](https://www.python.org/)
  * [FastAPI](https://fastapi.tiangolo.com/) - Framework web para construção da API.
  * [Google GenAI SDK](https://ai.google.dev/) - Integração com o modelo Gemini 2.0 Flash.
  * [Pydantic](https://www.google.com/search?q=https://docs.pydantic.dev/) - Validação de dados e estruturação de objetos.
  * [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI.

## 📂 Estrutura do Projeto

  * `src/main.py`: Ponto de entrada da API (Servidor FastAPI).
  * `src/interpretador.py`: Módulo responsável por "traduzir" a entrada do usuário em uma lista estruturada de tipos de perguntas usando IA.
  * `src/gerador.py`: Responsável por gerar o JSON específico de cada tipo de pergunta (com suas propriedades, labels e regras) usando o Gemini.
  * `src/montador.py`: Orquestra o processo, unindo os itens gerados, criando a estrutura de navegação e formatando o JSON final do instrumento (Survey).
  * `requirements.txt`: Lista de dependências do projeto.

## 🛠️ Instalação e Configuração

### 1\. Pré-requisitos

Certifique-se de ter o Python instalado. É recomendável o uso de um ambiente virtual.

### 2\. Instalação

Clone o repositório e instale as dependências:

```bash
# Clone o repositório (exemplo)
git clone https://github.com/seu-usuario/homero.git
cd homero

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3\. Configuração de Variáveis de Ambiente

O projeto requer uma chave de API do Google Gemini. Crie um arquivo `.env` na raiz do projeto seguindo o padrão utilizado no código:

```env
GEMINI_API_KEY=sua_chave_de_api_aqui
```

> **Nota:** O código carrega as variáveis usando `dotenv`. Certifique-se de que o arquivo `.env` esteja no mesmo nível que o script de execução ou configurado corretamente.

## ▶️ Como Usar

### Executando o Servidor

Para iniciar o servidor da API, execute o arquivo `src/main.py`:

```bash
python src/main.py
```

*Por padrão, o servidor está configurado no código para rodar no host `143.54.85.142` e porta `27017`. Caso esteja rodando localmente, você pode precisar ajustar essas configurações no final do arquivo `src/main.py` para `localhost` ou `0.0.0.0`.*

### Endpoints da API

#### `GET /`

Verifica se o servidor está online.

  - **Resposta:** `{"message": "homero-api-server"}`

#### `POST /survey/`

Gera um instrumento de pesquisa completo baseado em uma descrição.

  - **Payload (JSON):**

    ```json
    {
      "description": "Gere um formulário com uma pergunta de texto sobre o nome do paciente e uma pergunta de data sobre o nascimento."
    }
    ```

  - **Exemplo de Resposta (Simplificado):**

    ```json
    {
      "message": {
        "extents": "StudioObject",
        "objectType": "Survey",
        "identity": { ... },
        "itemContainer": [
            { "objectType": "TextQuestion", ... },
            { "objectType": "CalendarQuestion", ... }
        ],
        "navigationList": [ ... ]
      }
    }
    ```