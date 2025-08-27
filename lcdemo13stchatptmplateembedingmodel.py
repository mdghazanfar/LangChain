import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Load environment variables from .env file
load_dotenv()

# Get the secret key using getenv function
secret_key = os.getenv('OPENAI_API_KEY')

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", api_key=secret_key)
vectors = embedding_model.embed_documents("What are the top 2 most popular sports played in India")
# print(len(vectors))
# print(len(vectors[0]))

embedded_query = embedding_model.embed_query("What was the country name mentioned in the conversation?")
print(embedded_query[:5])
 




   
    

