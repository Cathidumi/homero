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

*Por padrão, o servidor está configurado no código para rodar no host homero.takere.com.br e porta `8080`. Caso esteja rodando localmente, você pode precisar ajustar essas configurações no final do arquivo `src/main.py` para `localhost` ou `0.0.0.0`.*

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

### 🛠️ Detalhamento: Função `generateJSON` (`montador.py`)

A função `generateJSON` atua como o **orquestrador principal** da solução recomendada. Ela é responsável por integrar a interpretação de linguagem natural, a geração de componentes isolados e a estruturação lógica do formulário final.

#### Assinatura

```python
def generateJSON(userInput: str, acID: str = 'TML', name: str = 'formulario') -> dict
```

#### Parâmetros

  * **`userInput`**: String contendo a descrição em linguagem natural do formulário desejado (ex: "Crie uma pesquisa com nome, idade e uma pergunta de múltipla escolha sobre frutas").
  * **`acID`**: (Opcional) O acrônimo base utilizado para gerar os identificadores únicos (`templateID` e `customID`) de cada item (Padrão: `'TML'`).
  * **`name`**: (Opcional) O nome interno atribuído ao objeto de identidade do formulário.

#### Fluxo de Processamento

A função executa quatro etapas críticas sequencialmente:

1.  **Geração de Conteúdo (`itemContainer`)**:

      * Invoca `generateItemContainer(userInput)`, que primeiramente chama o `userToAITranslator` para quebrar o pedido em uma lista de intenções estruturadas.
      * Itera sobre essas intenções e aciona funções geradoras específicas (como `textQuestion`, `integerQuestion`) para criar cada objeto JSON individualmente.

2.  **Cálculo de Navegação (`navigationList`)**:

      * Com base na contagem total de itens gerados, chama `generate_navigation_structure`.
      * Cria automaticamente o fluxo linear de navegação: *BEGIN NODE* → *Item 1* → *Item 2* → ... → *END NODE*, garantindo que o formulário seja funcional.

3.  **Normalização de Identificadores (Pós-processamento)**:

      * Executa um loop de correção sobre todos os itens gerados para padronizar os IDs.
      * Reescreve os campos `templateID` e `customID` sequencialmente (ex: `TML1`, `TML2`) para garantir consistência e unicidade, independentemente do que foi gerado pelo LLM.
      * Para questões do tipo `CheckboxQuestion`, também normaliza os IDs das opções internas (ex: `TML2a`, `TML2b`).

4.  **Montagem Final**:

      * Insere os contêineres de itens e navegação na estrutura base do objeto `Survey` (que contém metadados como `metainfo`, `identity`, etc.) e retorna o dicionário completo pronto para exportação.