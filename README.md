# homero
Solução para construção de instrumentos clínicos

Esta documentação explica o propósito do projeto, como instalá-lo, configurá-lo e utilizar a API para gerar instrumentos de pesquisa.

-----

# Homero

**Solução para construção automatizada de instrumentos clínicos e de pesquisa.**

O **Homero** é uma aplicação backend desenvolvida em Python que utiliza Inteligência Artificial Generativa para converter descrições em linguagem natural em estruturas JSON complexas de formulários de pesquisa. O sistema é capaz de interpretar solicitações de usuários e montar instrumentos completos compatíveis com padrões específicos (estrutura `StudioObject`/`SurveyItem`), incluindo lógica de navegação e metadados.

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
  * [OpenAI SDK] (https://developers.openai.com/api/docs) - Integração com LLMs
  * [Pydantic](https://www.google.com/search?q=https://docs.pydantic.dev/) - Validação de dados e estruturação de objetos.
  * [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI.

## 📂 Estrutura do Projeto

  * `src/gemini_app/main.py`: Ponto de entrada da API (Servidor FastAPI).
  * `src/gemini_app/interpretador.py`: Módulo responsável por "traduzir" a entrada do usuário em uma lista estruturada de tipos de perguntas usando IA.
  * `src/gemini_app/gerador.py`: Responsável por gerar o JSON específico de cada tipo de pergunta (com suas propriedades, labels e regras) usando LLM.
  * `src/gemini_app/montador.py`: Orquestra o processo, unindo os itens gerados, criando a estrutura de navegação e formatando o JSON final do instrumento (Survey).
  * `requirements.txt`: Lista de dependências do projeto.

## 🛠️ Instalação e Configuração

### 1\. Pré-requisitos

Certifique-se de ter o Python instalado. É recomendável o uso de um ambiente virtual.

### 2\. Instalação

Clone o repositório e instale as dependências:

```bash
# Clone o repositório (exemplo)
git clone link_do_repositorio
cd homero

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3\. Configuração de Variáveis de Ambiente

O projeto requer uma chave de API do OPENROUTER, podendo ser configurado para utilizar chaves do GEMINI e da OPENAI em conjunto. Crie um arquivo `.env` na raiz do projeto seguindo o padrão utilizado no código:

```env
OPENROUTER_API_KEY=sua_chave_de_api_aqui
```

> **Nota:** O código carrega as variáveis usando `dotenv`. Certifique-se de que o arquivo `.env` esteja no mesmo nível que o script de execução ou configurado corretamente.

## ▶️ Como Usar

### Executando o Servidor

Para iniciar o servidor da API, execute o arquivo `src/gemini_app/main.py`:

```bash
python src/gemini_app/main.py
```

*Por padrão, o servidor está configurado no código para rodar no `localhost` ou `0.0.0.0`. Você pode ajustar essas configurações no final do arquivo `src/gemini_app/main.py`.*

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
      "message":{

        "interpretation": [
          {"typeQuestion": "TextQuestion",
            "question": "Qual o nome do paciente?",
            "options": null
          },
          {"typeQuestion": "CalendarQuestion",
          "question": "Qual a data de nascimento do paciente?",
          "options": null
          }],

        "itemContainer": {...},

        "finalForm":  {
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
    }
    ```

Sendo o campo `finalForm` responsável por armazenar o questionário em sua forma final para importação na plataforma Otus Studio.

### 🛠️ Detalhamento: Função `generateJSON` (`montador.py`)

A função `generateJSON` atua como o **orquestrador principal** da solução. Ela é responsável por integrar a interpretação de linguagem natural, a geração de componentes isolados e a estruturação lógica do formulário final.

#### Assinatura

```python
def generateJSON(userInput: str, acID: str = 'TML', name: str = 'formulario', modelo: str = 'gpt-4o') -> dict
```

#### Parâmetros

  * **`userInput`**: String contendo a descrição em linguagem natural do formulário desejado (ex: "Crie uma pesquisa com nome, idade e uma pergunta de múltipla escolha sobre frutas").
  * **`acID`**: (Opcional) O acrônimo base utilizado para gerar os identificadores únicos (`templateID` e `customID`) de cada item (Padrão: `'TML'`).
  * **`name`**: (Opcional) O nome interno atribuído ao objeto de identidade do formulário.
  * **`modelo`**: (Opcional) Define o modelo a ser usado na geração do formulário (Padrão: `'gpt-4o'`).

#### Fluxo de Processamento

A função executa quatro etapas críticas sequencialmente:

1.  **Geração de Conteúdo (`itemContainer`)**:

      * Invoca `generateItemContainer()`, que primeiramente chama o `interpretador.py` para quebrar o pedido em uma lista de intenções estruturadas.
      * Itera sobre essas intenções e aciona funções geradoras específicas (como `textQuestion`, `integerQuestion`) para criar cada objeto JSON individualmente.

2.  **Cálculo de Navegação (`navigationList`)**:

      * Com base na contagem total de itens gerados, chama `generate_navigation_structure`.
      * Cria automaticamente o fluxo linear de navegação: *BEGIN NODE* → *Item 1* → *Item 2* → ... → *END NODE*, garantindo que o formulário seja funcional.

3.  **Normalização de Identificadores (Pós-processamento)**:

      * Executa um loop de correção sobre todos os itens gerados para padronizar os IDs.
      * Reescreve os campos `templateID` e `customID` sequencialmente (ex: `TML1`, `TML2`) para garantir consistência e unicidade, independentemente do que foi gerado pelo LLM.
      * Para questões do tipo `CheckboxQuestion`, também normaliza os IDs das opções internas (ex: `TML2a`, `TML2b`).

4.  **Montagem Final**:

      * Insere os contêineres de itens e navegação na estrutura base do objeto `Survey` (que contém metadados como `metainfo`, `identity`, etc.) e retorna o dicionário completo para exportação.

---

## 🔁 Implementação alternativa: openrouter_app

A pasta `openrouter_app` é outra implementação desta mesma ferramenta, seguindo a mesma lógica de geração e montagem de formulários, porém adaptada para uso com a API do OpenRouter. Sua utilização é semelhante à da implementação principal: o fluxo principal também envolve a interpretação da descrição do usuário, a geração dos itens do formulário e a montagem do JSON final para importação em plataformas de pesquisa.

Em outras palavras, `openrouter_app` funciona como uma variante equivalente do Homero, mantendo a mesma proposta de uso e estrutura de operação, mas com integração específica ao provedor OpenRouter.


