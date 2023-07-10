import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv 
import streamlit as st

_= load_dotenv(find_dotenv()) #read local.env file
openai.api_key = st.secrets["api_secret"]

def get_completion(prompt,model="gpt-3.5-turbo"):
    messages = [{"role":"user","content":prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temparature=0, #this is the degree of randomness         
    )
    return response.choices[0].message["content"]

response = get_completion("What is the capital of France?")
print(response)