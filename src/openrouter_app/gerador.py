
import os
from dotenv import load_dotenv
import interpretador
import json
from datetime import datetime

from openai import OpenAI


load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv('OPENROUTER_API_KEY'))

def singleSelectionQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content": """- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **SingleSelectionQuestion:{"extents":"SurveyItem","objectType":"SingleSelectionQuestion","templateID":"TML1","customID":"TML1","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"SingleSelectionQuestion input","formattedText":"SingleSelectionQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"options":[{"extents":"StudioObject","objectType":"AnswerOption","value":1,"extractionValue":1,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 1 input","formattedText":"option 1 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"AnswerOption","value":2,"extractionValue":2,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 2 input","formattedText":"option 2 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"AnswerOption","value":3,"extractionValue":3,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 3 input","formattedText":"option 3 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}],"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}},"imageUrl":null  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
      ],
        response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def checkboxQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **CheckboxQuestion:{"extents":"SurveyItem","objectType":"CheckboxQuestion","templateID":"TML2","customID":"TML2","dataType":"Array","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"CheckboxQuestion input","formattedText":"CheckboxQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"options":[{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2a","customOptionID":"TML2a","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 1 input","formattedText":"option 1 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2b","customOptionID":"TML2b","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 2 input","formattedText":"option 2 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2c","customOptionID":"TML2c","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 3 input","formattedText":"option 3 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}],"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def calendarQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **CalendarQuestion:{"extents":"SurveyItem","objectType":"CalendarQuestion","templateID":"TML3","customID":"TML3","dataType":"LocalDate","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"CalendarQuestion input","formattedText":"CalendarQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def integerQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **IntegerQuestion:{"extents":"SurveyItem","objectType":"IntegerQuestion","templateID":"TML4","customID":"TML4","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"IntegerQuestion input","formattedText":"IntegerQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"unit":{"ptBR":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""}},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def decimalQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **DecimalQuestion:{"extents":"SurveyItem","objectType":"DecimalQuestion","templateID":"TML5","customID":"TML5","dataType":"Decimal","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"DecimalQuestion input","formattedText":"DecimalQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"unit":{"ptBR":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""}},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def textQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TextQuestion:{"extents":"SurveyItem","objectType":"TextQuestion","templateID":"TML6","customID":"TML6","dataType":"String","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TextQuestion input","formattedText":"TextQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def emailQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **EmailQuestion:{"extents":"SurveyItem","objectType":"EmailQuestion","templateID":"TML7","customID":"TML7","dataType":"String","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"EmailQuestion input","formattedText":"EmailQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def timeQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TimeQuestion:{"extents":"SurveyItem","objectType":"TimeQuestion","templateID":"TML8","customID":"TML8","dataType":"LocalTime","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TimeQuestion input","formattedText":"TimeQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}},"options":{"extends":"StudioObject","objectType":"QuestionOption","data":{}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def phoneQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **PhoneQuestion:{"extents":"SurveyItem","objectType":"PhoneQuestion","templateID":"TML9","customID":"TML9","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"PhoneQuestion input","formattedText":"PhoneQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def textItem(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TextItem:{"extents":"SurveyItem","objectType":"TextItem","templateID":"TML10","customID":"TML10","dataType":"String","value":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TextItem input","formattedText":"TextItem input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def autocompleteQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **AutocompleteQuestion: {"extents":"SurveyItem","objectType":"AutocompleteQuestion","templateID":"TML11","customID":"TML11","dataType":"String","dataSources":[],"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"AutocompleteQuestion input","formattedText":"AutocompleteQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def fileUploadQuestion(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **FileUploadQuestion: {"extents":"SurveyItem","objectType":"FileUploadQuestion","templateID":"TML12","customID":"TML12","dataType":"Binary","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"FileUploadQuestion input","formattedText":"FileUploadQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def imageItem(userInput, modelo):
    itensCompletion = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content":"""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **ImageItem: {"extents":"SurveyItem","objectType":"ImageItem","templateID":"TML13","customID":"TML13","dataType":"String","url":"","footer":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        },
        {
            "role": "user",
            "content": f"**user input**: Generate a json with {userInput}"
        }
    ],
    response_format={"type": "json_object"}
    )
    return itensCompletion.choices[0].message.content

def generateItemContainer(userInput, modelo):
    load_dotenv()
    API_KEY = os.getenv('OPENROUTER_API_KEY')
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=API_KEY)

    promptList = interpretador.translation(userInput, modelInterpreter=modelo)
    if 'error' in promptList:
        print('erro na interpretação')
        generationLog = {"interpretation": str(promptList), "itemContainer": None, "error": f"Error during interpretation"} #create a dict to log the interpretation, the generated item container and the error message
        return generationLog #return dict object containing all generated elements and the error message

    itemContainer = {"itemContainer": []}
    element = ''
    print('Gerando item container...')
    for prompt in promptList:
        #print(prompt["typeQuestion"])
        element = ''
        match prompt["typeQuestion"]:
            case "SingleSelectionQuestion":
                element = singleSelectionQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = singleSelectionQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "CheckboxQuestion":
                element = checkboxQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = checkboxQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "CalendarQuestion":
                element = calendarQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = calendarQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "IntegerQuestion":
                element = integerQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = integerQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "DecimalQuestion":
                element = decimalQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = decimalQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "TextQuestion":
                element = textQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = textQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "EmailQuestion":
                element = emailQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = emailQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "TimeQuestion":
                element = timeQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = timeQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "PhoneQuestion":
                element = phoneQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = phoneQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "TextItem":
                element = textItem(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = textItem(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "AutocompleteQuestion":
                element = autocompleteQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = autocompleteQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "FileUploadQuestion":
                element = fileUploadQuestion(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = fileUploadQuestion(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "ImageItem":
                element = imageItem(json.dumps(prompt), modelo=modelo)
                try:
                    element_json = json.loads(element) #try to parse the element as JSON
                except json.JSONDecodeError:
                    element = imageItem(json.dumps(prompt), modelo=modelo) #if it fails, try to generate the element again
            case "GridIntegerQuestion":
                pass
            case "GridTextQuestion":
                pass
            case _:
                pass
        try:
            itemContainer["itemContainer"].append(json.loads(element)) #append element to the list inside itemContainer Field
        except json.JSONDecodeError:
            print('Erro na geração de item')
            itemContainer["itemContainer"].append(element) #if the element is not a valid JSON, append it as a string to the list inside itemContainer Field
            generationLog = {"interpretation": promptList, "itemContainer": itemContainer["itemContainer"], "error": f"Error decoding JSON for element"} #create a dict to log the interpretation, the generated item container and the error message
            return generationLog #return dict object containing all generated elements and the error message
        except Exception as e:
            print('Erro inesperado no item container')
            itemContainer["itemContainer"].append(element) #if any other error occurs, append the element as a string to the list inside itemContainer Field
            generationLog = {"interpretation": promptList, "itemContainer": itemContainer["itemContainer"], "error": f"Unexpected error for element, error message: {str(e)}"} #create a dict to log the interpretation, the generated item container and the error message
            return generationLog #return dict object containing all generated elements and the error message

    generationLog = {"interpretation": promptList,
                     "itemContainer": itemContainer["itemContainer"]} #create a dict to log the interpretation and the generated item container
    print('Item container gerado com sucesso')
    return generationLog #return dict object containing all generated elements

def generate_navigation_structure(num_elements=int, acID='TML'):
    # Define the list for storing the navigation elements
    navigation_list = []

    # Add the BEGIN NODE
    begin_node = {
        "extents": "SurveyTemplateObject",
        "objectType": "Navigation",
        "origin": "BEGIN NODE",
        "index": 0,
        "inNavigations": [],
        "routes": [{"extents": "SurveyTemplateObject",
                    "objectType": "Route",
                    "origin": "BEGIN NODE",
                    "destination": f"{acID}1",
                    "name": f"BEGIN NODE_{acID}1",
                    "isDefault": True,
                    "conditions": []}]
    }
    navigation_list.append(begin_node)

    # Add the END NODE with placeholder for inNavigations, to fill after adding intermediate nodes
    end_node = {
        "extents": "SurveyTemplateObject",
        "objectType": "Navigation",
        "origin": "END NODE",
        "index": 1,
        "inNavigations": [None] * 2,  # Placeholder for inNavigations
        "routes": []
    }
    navigation_list.append(end_node)

    # Add intermediate acID nodes
    for i in range(num_elements):
        origin = f"{acID}{i + 1}"
        # Destination acID or END NODE
        destination = f"{acID}{i + 2}" if i + 1 < num_elements else "END NODE"

        # Create acID node
        acID_node = {
            "extents": "SurveyTemplateObject",
            "objectType": "Navigation",
            "origin": origin,
            "index": i + 2,
            "inNavigations": [{"origin": f"BEGIN NODE" if i == 0 else f"{acID}{i}", "index": i + 1}],
            "routes": [{"extents": "SurveyTemplateObject",
                        "objectType": "Route",
                        "origin": origin,
                        "destination": destination,
                        "name": f"{origin}_{destination}",
                        "isDefault": True,
                        "conditions": []}]
        }
        navigation_list.append(acID_node)

    # Fill inNavigations for END NODE to point to the last acID node
    if num_elements > 0:
        end_node["inNavigations"] = [None, {"origin": f"{acID}{num_elements}", "index": 1 + num_elements + 1}]

    return {"navigationList": navigation_list}

