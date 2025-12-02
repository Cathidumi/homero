#imports for server 
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
#custom imports
import os
import montador
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
    
if __name__ == "__main__":
    hostIP = os.getenv('HOST_IP')
    uvicorn.run(app, host=hostIP, port=8080)
