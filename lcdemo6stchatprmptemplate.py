import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()

# Get the secret key using getenv function
secret_key = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model = "gpt-4o-mini", api_key = secret_key)

st.title("Sports-Arena")
given_country = st.text_input("Enter the country name:")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in sports and general knowledge."),
    ("human", "What are the top 3 most popular sports played in {country}?"),
])

if given_country:
    # Format the prompt with the country
    formatted_prompt = prompt_template.format_messages(country=given_country)
    # Invoke the model with the formatted prompt
    response = model.invoke(formatted_prompt)
    st.write(response.content)
