#imports for server 
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json

#custom imports
import os
import montador
import interpretador

#import env variables
from dotenv import load_dotenv
load_dotenv()#loads env variables

class Survey(BaseModel):
    description: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "homero-api-server"}

@app.get("/get-survey/")
async def get_survey():
    userForm = 'one text item element'
    generatedJSON = montador.generateJSON(userForm)
    return {"message": generatedJSON}

@app.post("/survey/")
async def create_survey(survey: Survey):
    userForm = survey.description
    generatedJSON = montador.generateJSON(userForm)
    return {"message": generatedJSON}

@app.post("/structure/")
async def create_survey_structure(survey: Survey):
    userForm = survey.description
    try:
        interpretedJSON = interpretador.translation(userForm)
        interpretedJSON = json.loads(interpretedJSON)
    except Exception as e:
        return {"error": str(e)}
    return {"message": interpretedJSON}
    
if __name__ == "__main__":
    hostIP = os.getenv('HOST_IP')
    #hostIP = 'localhost'    #testing purposes
    uvicorn.run(app, host=hostIP, port=8080)
