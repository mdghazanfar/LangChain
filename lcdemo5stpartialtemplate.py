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
# country1 = st.text_input("Enter the First country name:")
country2 = st.text_input("Enter the country name that you campare with India:")
year = st.text_input("Enter the year:")

# Prompt template
prompt_template = PromptTemplate(
    input_variables=["country1","country2",  "year"],
    template="""
    You are an expert in GK.
    Answer the question: How many medals in olympics won by the {country1}  or {country2} in the year {year} ?
    """,
    partial_variables={
        "country1" : "India"
    }
)

if country2 and year:
    response = model.invoke(prompt_template.format(country2=country2, year = year))
    st.write(response.content)