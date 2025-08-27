import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import List, Dict

# Load environment variables from .env file
load_dotenv()

# Get the secret key using getenv function
secret_key = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model = "gpt-4o-mini", api_key = secret_key)

# Define the JSON structure we expect
parser = JsonOutputParser(pydantic_object={
    "type": "object",
    "properties": {
        "sports": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "popularity_rank": {"type": "integer"},
                    "description": {"type": "string"}
                },
                "required": ["name", "popularity_rank", "description"]
            }
        }
    },
    "required": ["sports"]
})

st.title("Sports-Arena with JSON Output")
given_country = st.text_input("Enter the country name:")

# Modified prompt template with escaped curly braces for the JSON structure
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are an expert in sports and general knowledge. 
    Provide information about sports in JSON format with the specified structure."""),
    ("human", """What are the top 3 most popular sports played in {country}? 
    Return the response in the following JSON format:
    {{
        "sports": [
            {{
                "name": "sport name",
                "popularity_rank": 1,
                "description": "brief description"
            }}
        ]
    }}"""),
])

if given_country:
    # Chain the prompt template with the model and JSON parser
    chain = prompt_template | model | parser
    
    try:
        response = chain.invoke({"country": given_country})
        
        # Display the results in a more structured way
        st.subheader(f"Popular Sports in {given_country}")

        # print the response in JSON Format in the browser using Streamlit
        st.write(response)
        
        # printing eachsport with name, rank and description in presentable way in the UI
        # for sport in response["sports"]:
        #     with st.expander(f"{sport['name']} (Rank: {sport['popularity_rank']})"):
        #         st.write(sport['description'])
          
        
    except Exception as e:
        st.error(f"Error parsing response: {str(e)}")
