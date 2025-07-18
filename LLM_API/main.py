from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
from dotenv import load_dotenv
import os

load_dotenv()

API_KEYS_CREDITS = {os.getenv("API_KEY"): 10}

app = FastAPI()
# initiating the api

# will look into the header of the request to find the variable x_api_key
def verify_api_key(x_api_key:str = Header(None)): 
    credits = API_KEYS_CREDITS.get(x_api_key,0)
    if credits <=0:
        raise HTTPException(status_code = 401, detail="Invalid API Key, or no credits")

    return x_api_key


@app.post("/generate")
def generate(prompt: str, x_api_key:str = Depends(verify_api_key)):
    API_KEYS_CREDITS[x_api_key] -= 1
    reponse = ollama.chat(model='mistral', messages = [{'role':"user", "content": prompt}])   #the messages dict is the input to the model giving it instructions on what and how to do 
    #  for example messages = [{'role':"system", 'content':"You are a poetic assistant who answers in rhymes."},{'role':"user", "content": prompt}])
    return {"response": reponse['message']['content']}
    # the response generated by model generally follow the same format where in a dictiory various things are given in which the message dict is there containing the main output 



