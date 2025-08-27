import os
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get the secret key using getenv function
secret_key = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model = "gpt-4o-mini", api_key = secret_key )

st.title("Gen AI - Sample app")
prompt = st.text_input("Please ask your question")

response = model.invoke(prompt)

# print the response on the browser using streamlit
st.write(response)

# Comment line number 23, and execute the below, observe the response in the browser
# st.write(response.content)