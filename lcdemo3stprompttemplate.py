import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Get the secret key using getenv function
secret_key = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model = "gpt-4o-mini", api_key = secret_key )

st.title("Sports-Arena")
country = st.text_input("Enter the country name:")

prompt_template = PromptTemplate(
    input_variables=["country"],
    template="""
    You are an expert in GK.
    Answer the question: What are the three top sports palyed in{country}?
    """
)

if country:
    response = model(prompt_template.format(country=country))
    # Observe the terminal for the deprecation warning 
    st.write(response.content)