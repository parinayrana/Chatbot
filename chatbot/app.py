from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## environments variable call

os.environ["OPENAI_API_KEY"]=   os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")

##creating chatbot 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful mentor cum assistant. Please provde responses in a philosphical practical way taking references from the stoic writings"),
        ("user", "Question:{question}")
    ]
)

#streamlit framework

st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the things you want assistance in")

#open ai llm call 
llm = ChatOpenAI(model='gpt-3.5-turbo-0125')
output_parser = StrOutputParser()

# chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


#token limit exceeded error in openai 
#will switch to opensource
