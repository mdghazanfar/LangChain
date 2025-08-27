import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough

# Load environment variables from .env file
load_dotenv()

# Get the secret key using getenv function
secret_key = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model="gpt-4o-mini", api_key=secret_key, streaming=True)

# Create a simple prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in sports and general knowledge."),
    ("human", "What are the top 2 most popular sports played in {country}?"),
])

given_country = st.text_input("Enter the country name:")

if given_country:
    # Chains are easily reusable components linked together.
    # Chains encode a sequence of calls to components like models, document retrievers, other Chains, etc., 
    # and provide a simple interface to this sequence.
    
    chain = prompt_template | model
    #response = chain.invoke({"country": given_country})

    message_placeholder = st.empty()
    full_response = ""

    # Stream the response token by token
    # for chunk in chain.stream({"country": given_country}):
    #     if chunk is not None:
    #        # print(chunk.content, end=",", flush=True)

    # stream the response token by token and Observe the response on the browser
    for chunk in chain.stream({"country": given_country}):
        if chunk is not None:
            full_response += chunk.content
            message_placeholder.write(full_response)
                




   
    

