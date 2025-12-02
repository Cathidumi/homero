import gerador
import json
from datetime import datetime

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

    itemCont = gerador.generateItemContainer(userInput) #generates item container field

    form['itemContainer'] = itemCont['itemContainer'] #adds generated field to forms dictionary

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
        
    return form #retorna dicionario que deve ser convertido para json na exportação

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

    mydirectory = '/home/caua/Documents/homero/samples/' #directory where samples are saved
    with open(f'{mydirectory}/sample_{getTime()}.json', 'w') as outfile:
        json.dump(generatedForm, outfile)