import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional

from openai import OpenAI


load_dotenv()

class Question(BaseModel):
  typeQuestion: str
  question: str
  options: Optional[list[str]]

class Questions(BaseModel):
  questions: list[Question]


def translation(userInput, modelInterpreter='gpt-4o'):
  load_dotenv()
  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
  )
  print('Gerando interpretação')
  try:
    response = client.responses.parse(
      model=modelInterpreter,
      input=[
        {
          "role": "system",
          "content": """- You are a helpful assistant whose task is to put information in a structured json
              - This json will further be user for another assistant in an forms aplication.  
              - The list of possible types for a question is: [SingleSelectionQuestion, CheckboxQuestion, CalendarQuestion, IntegerQuestion, DecimalQuestion, TextQuestion, EmailQuestion, TimeQuestion, PhoneQuestion, TextItem]
              - Fill the json properties as resquested by the user input
              - Do it step by step as specified by the system structure.
              - Generate a response without lines and spaces"""
        },
        {
          "role": "user",
          "content": f"**userInput:**{userInput}"
        }
      ],
      text_format=Questions
    )
  except Exception as e:
    return ['error', f'Error generating response, error message: {str(e)}', str(response)]
  
  try:
    questoes = response.output_parsed.__dict__
  except Exception as e:
    questoes = response.output_text
    return ['error', f'Error parsing response, error message: {str(e)}', str(questoes)]
  
  lista_questoes = questoes['questions']

  try:
    lista_questoes = [quest.__dict__ for quest in lista_questoes]
  except Exception as e:
    return ['error', f'Error converting questions to list of dicts, error message: {str(e)}', str(lista_questoes)]
  
  print(lista_questoes)
  return lista_questoes


if __name__ == "__main__":
  generatedJson = translation(
    """Estrutura das Perguntas
1. Qual é o principal motivo da sua vinda à unidade de saúde hoje?

Tipo: Resposta Curta (Objetiva).

Objetivo: Identificar a queixa principal.

"""
  )
