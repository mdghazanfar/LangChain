import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

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
    # Chains are easily reusable components linked together.
    # Chains encode a sequence of calls to components like models, document retrievers, other Chains, etc., 
    # and provide a simple interface to this sequence.
    
    chain = prompt_template | model | StrOutputParser()
    response = chain.invoke({"country": given_country})

    output_parser = StrOutputParser()
    st.write(output_parser.parse(response))