import os
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional
from google.genai import types


load_dotenv()

class Translator(BaseModel):
  typeQuestion: str
  question: str
  options: Optional[list[str]]

def translation(userInput):
  client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
  response = client.models.generate_content(
      model='gemini-2.0-flash',
      contents=f"**userInput:**{userInput}",
      config=types.GenerateContentConfig(
        response_mime_type='application/json',
        response_schema= list[Translator],
        system_instruction="""- You are a helpful assistant whose task is to put information in a structured json
              - This json will further be user for another assistant in an forms aplication.  
              - The list of possible types for a question is: [SingleSelectionQuestion, CheckboxQuestion, CalendarQuestion, IntegerQuestion, DecimalQuestion, TextQuestion, EmailQuestion, TimeQuestion, PhoneQuestion, TextItem]
              - Fill the json properties as resquested by the user input
              - Do it step by step as specified by the system structure.
              - Generate a response without lines and spaces"""
      )
  )
  generatedJson = response.text
  #print(generatedJson)
  return generatedJson
  

if __name__ == "__main__":
  generatedJson = translation('Gere um json com duas perguntas genéricas')
  print(generatedJson)

# -Translate this: **one SingleSelectionQuestion item, with the following question: 'What is your City?' with the following options: 'Porto', 'Alegrete', 'Viamao'. Include one CheckboxQuestion item with the following question: 'what is do you eat?' with the following options: 'meat', 'vegetables'. Include one CalendarQuestion with the following question: 'When is your birthday?'. Include one IntegerQuestion with the following question: 'How Old are you?**