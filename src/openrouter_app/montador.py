import gerador
import json
from datetime import datetime
import os

def generateJSON(userInput=str, acID='TML', name='formulario', modelo='gpt-4o'):
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

    generationLog = gerador.generateItemContainer(userInput, modelo=modelo) #generates item container field

    # Encerra em caso de erro na geração de itens
    if 'error' in generationLog:
        return generationLog
     
    form['itemContainer'] = generationLog['itemContainer'] #adds generated field to forms dictionary

    numOfItens = len(form['itemContainer'])

    #print('Generating navigation...')

    navigationList = gerador.generate_navigation_structure(numOfItens)

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

    generationLog['finalForm'] = form #add final form structure to generation log    
    return generationLog #retorna dicionario que deve ser convertido para json na exportação

def getTime():
    currentTime = str(datetime.now())
    currentTime = currentTime.replace(' ', 'T')
    currentTime = currentTime.replace(':', '_')
    currentTime = currentTime[:19]
    return currentTime


if __name__ == "__main__":

    listaModelos = ['google/gemini-2.0-flash-001', 'gpt-4o', 'openai/gpt-4o-mini','google/gemini-2.5-flash-lite' ,'google/gemini-2.5-flash']
    
    #formulário de entrada
    inputForm = int(input('Digite o número do questionário (3 a 10): '))
    form = f'quest{inputForm}.txt'
    formNumber = form.replace('.txt', '')

    #ajustando diretório para ler os formulários de entrada
    questdirectory = os.path.dirname(os.path.abspath(__file__))
    questdirectory = questdirectory.replace('experimentos', 'questforms')
    questdirectory = questdirectory.replace('/modularOpenrouter', '')


    with open (f'{questdirectory}/{form}', 'r') as file:
        userForm = file.read()

    #ajustando diretório para salvar os formulários gerados
    mydirectory = os.path.dirname(os.path.abspath(__file__))
    mydirectory = mydirectory.replace('experimentos', 'samples')
    mydirectory = mydirectory.replace('/modularOpenrouter', f'/{formNumber}')
    if not os.path.exists(mydirectory):
        os.makedirs(mydirectory)

    for model in listaModelos:
        if model == 'google/gemini-2.0-flash-001':
            experiment = 'sample_MO_Gemini20Flash'
        elif model == 'gpt-4o' or model == 'openai/gpt-4o':
            experiment = 'sample_MO_GPT4o'
        elif model == 'openai/gpt-4o-mini':
            experiment = 'sample_MO_GPT4oMini'
        elif model == 'google/gemini-2.0-flash-lite-001':
            experiment = 'sample_MO_Gemini20FlashLite'
        elif model == 'google/gemini-2.5-flash-lite':   
            experiment = 'sample_MO_Gemini25FlashLite'
        elif model == 'google/gemini-2.5-flash':
            experiment = 'sample_MO_Gemini25Flash'
        elif model == 'google/gemini-2.5-pro':
            experiment = 'sample_MO_Gemini25Pro'
        else:
            experiment = 'sample_MO_OpenRouter'
        for i in range(1): #number of forms to be generated
            tempo = getTime() #get current time to be used in file name
            try:
                print(f'Tentativa formulário {experiment}...')
                generatedLog = generateJSON(
                    userInput=userForm,
                    acID='TML',
                    name='formularioTeste',
                    modelo=model)


                #salvando log
                with open(f'{mydirectory}/log_{experiment}_{tempo}.json', 'w') as log_file:
                        json.dump(generatedLog, log_file) #save generation log for analysis

                if 'finalForm' in generatedLog:
                    generatedForm = generatedLog['finalForm'] #get final form structure from generation log
                    with open(f'{mydirectory}/{experiment}_{tempo}.json', 'w') as json_file:
                        json.dump(generatedForm, json_file) #save generated form as json file
                else:
                    print(f'Formulário {experiment} gerado com erros, verifique o log para mais detalhes.')

            except Exception as e:
                print(f'Error generating form {experiment}: {e}')
                with open(f'{mydirectory}/error_log_{experiment}_{tempo}.txt', 'a') as error_file:
                    error_file.write(f'{getTime()} - Error generating form {experiment}: {e}\n')
                pass
