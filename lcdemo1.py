import getpass
import os
from langchain_openai import ChatOpenAI

# load the environment using os library
if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# Open AI model = gpt-4o-mini
model = ChatOpenAI(model="gpt-4o-mini")

#  send the question to LLM, response stored in response variable
response = model.invoke("what is capital of India")

# print the response content
print(response.content)