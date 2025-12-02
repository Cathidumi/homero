
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import userToAITranslator
import json
from datetime import datetime

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def singleSelectionQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **SingleSelectionQuestion:{"extents":"SurveyItem","objectType":"SingleSelectionQuestion","templateID":"TML1","customID":"TML1","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"SingleSelectionQuestion input","formattedText":"SingleSelectionQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"options":[{"extents":"StudioObject","objectType":"AnswerOption","value":1,"extractionValue":1,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 1 input","formattedText":"option 1 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"AnswerOption","value":2,"extractionValue":2,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 2 input","formattedText":"option 2 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"AnswerOption","value":3,"extractionValue":3,"imageUrl":null,"imageTitle":false,"dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 3 input","formattedText":"option 3 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}],"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}},"imageUrl":null  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def checkboxQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **CheckboxQuestion:{"extents":"SurveyItem","objectType":"CheckboxQuestion","templateID":"TML2","customID":"TML2","dataType":"Array","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"CheckboxQuestion input","formattedText":"CheckboxQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"options":[{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2a","customOptionID":"TML2a","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 1 input","formattedText":"option 1 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2b","customOptionID":"TML2b","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 2 input","formattedText":"option 2 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}},{"extents":"StudioObject","objectType":"CheckboxAnswerOption","optionID":"TML2c","customOptionID":"TML2c","dataType":"Boolean","value":false,"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"option 3 input","formattedText":"option 3 input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}],"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def calendarQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **CalendarQuestion:{"extents":"SurveyItem","objectType":"CalendarQuestion","templateID":"TML3","customID":"TML3","dataType":"LocalDate","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"CalendarQuestion input","formattedText":"CalendarQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def integerQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **IntegerQuestion:{"extents":"SurveyItem","objectType":"IntegerQuestion","templateID":"TML4","customID":"TML4","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"IntegerQuestion input","formattedText":"IntegerQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"unit":{"ptBR":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""}},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def decimalQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **DecimalQuestion:{"extents":"SurveyItem","objectType":"DecimalQuestion","templateID":"TML5","customID":"TML5","dataType":"Decimal","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"DecimalQuestion input","formattedText":"DecimalQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"unit":{"ptBR":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Unit","oid":"","plainText":"","formattedText":""}},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def textQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TextQuestion:{"extents":"SurveyItem","objectType":"TextQuestion","templateID":"TML6","customID":"TML6","dataType":"String","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TextQuestion input","formattedText":"TextQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def emailQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **EmailQuestion:{"extents":"SurveyItem","objectType":"EmailQuestion","templateID":"TML7","customID":"TML7","dataType":"String","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"EmailQuestion input","formattedText":"EmailQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def timeQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TimeQuestion:{"extents":"SurveyItem","objectType":"TimeQuestion","templateID":"TML8","customID":"TML8","dataType":"LocalTime","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TimeQuestion input","formattedText":"TimeQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}},"options":{"extends":"StudioObject","objectType":"QuestionOption","data":{}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def phoneQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **PhoneQuestion:{"extents":"SurveyItem","objectType":"PhoneQuestion","templateID":"TML9","customID":"TML9","dataType":"Integer","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"PhoneQuestion input","formattedText":"PhoneQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def textItem(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **TextItem:{"extents":"SurveyItem","objectType":"TextItem","templateID":"TML10","customID":"TML10","dataType":"String","value":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"TextItem input","formattedText":"TextItem input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}  }**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def autocompleteQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **AutocompleteQuestion: {"extents":"SurveyItem","objectType":"AutocompleteQuestion","templateID":"TML11","customID":"TML11","dataType":"String","dataSources":[],"label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"AutocompleteQuestion input","formattedText":"AutocompleteQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def fileUploadQuestion(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **FileUploadQuestion: {"extents":"SurveyItem","objectType":"FileUploadQuestion","templateID":"TML12","customID":"TML12","dataType":"Binary","label":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"FileUploadQuestion input","formattedText":"FileUploadQuestion input"},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}},"metadata":{"extents":"StudioObject","objectType":"MetadataGroup","options":[]},"fillingRules":{"extends":"StudioObject","objectType":"FillingRules","options":{"mandatory":{"extends":"StudioObject","objectType":"Rule","validatorType":"mandatory","data":{"canBeIgnored":false,"reference":true}}}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def imageItem(userInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            response_mime_type='application/json',
            system_instruction="""- You are a helpful AI assistant capable of generating JSONs based on user input
        - These JSONs are responsible for creating forms in an external appication.
        - Your task is to generate JSONs objects that are based in the following JSON as specified by user input:

                **ImageItem: {"extents":"SurveyItem","objectType":"ImageItem","templateID":"TML13","customID":"TML13","dataType":"String","url":"","footer":{"ptBR":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"enUS":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""},"esES":{"extends":"StudioObject","objectType":"Label","oid":"","plainText":"","formattedText":""}}}**

        - Fill the correct properties inside the JSON structure.
        - Do it step by step as specified by the system structure.
        - Return it as a raw JSON, without spaces."""
        ),
        contents=f"**user input**: Generate a json with {userInput}"
    )
    return response.text

def generateItemContainer(userInput):
    promptList = json.loads(userToAITranslator.translation(userInput))
    itemContainer = {"itemContainer": []}
    #promptList = json.loads('[{"typeQuestion":"TextQuestion","question":"Enter your name","options":null},{"typeQuestion":"IntegerQuestion","question":"Enter your age","options":null}]')
    element = ''

    for prompt in promptList:
        print(prompt["typeQuestion"])
        element = ''
        match prompt["typeQuestion"]:
            case "SingleSelectionQuestion":
                element = singleSelectionQuestion(json.dumps(prompt))
            case "CheckboxQuestion":
                element = checkboxQuestion(json.dumps(prompt))
            case "CalendarQuestion":
                element = calendarQuestion(json.dumps(prompt))
            case "IntegerQuestion":
                element = integerQuestion(json.dumps(prompt))
            case "DecimalQuestion":
                element = decimalQuestion(json.dumps(prompt))
            case "TextQuestion":
                element = textQuestion(json.dumps(prompt))
            case "EmailQuestion":
                element = emailQuestion(json.dumps(prompt))
            case "TimeQuestion":
                element = timeQuestion(json.dumps(prompt))
            case "PhoneQuestion":
                element = phoneQuestion(json.dumps(prompt))
            case "TextItem":
                element = textItem(json.dumps(prompt))
            case "AutocompleteQuestion":
                element = autocompleteQuestion(json.dumps(prompt))
            case "FileUploadQuestion":
                element = fileUploadQuestion(json.dumps(prompt))
            case "ImageItem":
                element = imageItem(json.dumps(prompt))
            case "GridIntegerQuestion":
                pass
            case "GridTextQuestion":
                pass
            case _:
                pass
        itemContainer["itemContainer"].append(json.loads(element))#append element to the list inside itemContainer Field
    
    return itemContainer #return dict object containing all generated elements

def generateJSON(userInput=str, acID='TML', name='formulario'):
    """Generates the full JSON form structure based on user input description,
    including itemContainer and navigationList fields."""
    form = {
        "extents": "StudioObject",
        "objectType": "Survey",
        "oid": "dXNlclVVSUQ6W3VuZGVmaW5lZF1zdXJ2ZXlVVUlEOltkMzllZTg5MC05MDhkLTExZWYtOWZmYS1jOTM3YmMwNTQ1ODddcmVwb3NpdG9yeVVVSUQ6WyBOb3QgZG9uZSB5ZXQgXQ==",
        "identity": {
            "extents": "StudioObject",
            "objectType": "SurveyIdentity",
            "name": name,
            "acronym": acID,
            "recommendedTo": "",
            "description": "",
            "keywords": []
        },
        "metainfo": {
            "extents": "StudioObject",
            "objectType": "SurveyMetaInfo",
            "creationDatetime": "2024-10-22T15:53:48.697Z",
            "otusStudioVersion": ""
        },
        "dataSources": [],
        "itemContainer": [],
        "navigationList": [],
        "staticVariableList": [],
        "surveyItemGroupList": []
    }

    #print("Generating items...")

    itemCont = generateItemContainer(userInput) #generates item container field

    form['itemContainer'] = itemCont['itemContainer'] #adds generated field to forms dictionary

    numOfItens = len(form['itemContainer'])

    #print('Generating navigation...')

    navigationList = generate_navigation_structure(numOfItens)

    form['navigationList'] = navigationList['navigationList']

    #print('Adjusting indexes...')

    acronym = form['identity']['acronym']
    numOfItens = len(form['itemContainer'])
    alphaArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(0, numOfItens):
        form['itemContainer'][i]['templateID'] = f'{acronym}{i+1}'
        form['itemContainer'][i]['customID'] = f'{acronym}{i+1}'

        if form['itemContainer'][i]['objectType'] == 'CheckboxQuestion':
            currentIndex = form['itemContainer'][i]['templateID']
            for j in range(0, len(form['itemContainer'][i]['options'])):
                form['itemContainer'][i]['options'][j]['optionID'] = f'{acronym}{i+1}{alphaArray[j]}'
                form['itemContainer'][i]['options'][j]['customOptionID'] = f'{acronym}{i+1}{alphaArray[j]}'
        
    return form #retorna dicionario que deve ser convertido para json na exportação

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

def getTime():
    currentTime = str(datetime.now())
    currentTime = currentTime.replace(' ', 'T')
    currentTime = currentTime.replace(':', '_')
    currentTime = currentTime[:19]
    return currentTime

if __name__ == "__main__":

    userForm = str(input('Gere um instrumento de pesquisa com os seguintes itens:\n'))
    generatedForm = generateJSON(
        userInput=userForm,
        acID='TML',
        name='formularioTeste')
    print(generatedForm)

    mydirectory = '/home/caua/Documents/llm-tests/samples/gemini' #directory where samples are saved
    with open(f'{mydirectory}/sample_{getTime()}.json', 'w') as outfile:
        json.dump(generatedForm, outfile)
    