from fastapi import FastAPI
import ollama

app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
    reponse = ollama.chat(model='mistral', messages = [{'role':"user", "content": prompt}])
    return {"response": reponse['messages']['content']}