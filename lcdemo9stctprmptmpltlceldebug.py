from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the secret key using getenv function
secret_key = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model = "gpt-4o-mini", api_key = secret_key)

# First ChatPromptTemplate for country-specific sports
country_sports_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in sports and general knowledge."),
    ("human", "What are the top 3 most popular sports played in {country}?"),
]
)

# Second ChatPromptTemplate for specific sport information
sport_info_template = ChatPromptTemplate.from_template(
    """Provide detailed information about {sport} in {country}, including:
    1. Basic rules
    2. Major competitions
    """
)

# Final template combining both country and sport information
final_info_template = ChatPromptTemplate.from_template(
    """For {country}:
    First, list the top 3 sports: {country_sports}
    
    Then, for each sport mentioned, provide details:
    {sport_details}
    """
)

# Create LCEL chains
country_chain = country_sports_template | model 
sport_chain = sport_info_template | model
final_chain = final_info_template | model

# Streamlit UI
def main():
    st.title("Sports Arena")
    
    # Input for country
    country = st.text_input("Enter a country name:")
    
    # Dropdown for sports
    sports_list = ["Select your sport", "Football (Soccer)", "Basketball", "Tennis", "Cricket", "Rugby", "Baseball", "Volleyball", "Ice Hockey", "Golf", "Athletics"]
    
    selected_sport = st.selectbox("Select a sport:", sports_list, index=0)
    
    if country and selected_sport != "Select your sport":
        with st.spinner(f"Getting sports information..."):
            # Get country-specific sports and sport details
            country_sports = country_chain.invoke({"country": country})
            sport_result = sport_chain.invoke({"sport": selected_sport, "country": country})
            
            # Combine results using final chain
            final_result = final_chain.invoke({
                "country": country,
                "country_sports": country_sports,
                "sport_details": sport_result
            })
            
            st.write(final_result)

if __name__ == "__main__":
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        st.error("Please set your OpenAI API key in the environment variables!")
    else:
        main()
