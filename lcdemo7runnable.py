
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
import streamlit as st

class GreetingRunnable(Runnable):
    def __init__(self):
        self.config = RunnableConfig(max_tokens=50, temperature=0.7)

    def invoke(self, input: dict, config: RunnableConfig = None) -> str:
        country = input.get("country", "User") 
        return f"You wish to check the sports of this, {country}!"

    def batch(self, inputs: list, config: RunnableConfig = None) -> list:
        return [self.invoke(input) for input in inputs]

    def stream(self, input: dict, config: RunnableConfig = None):
        yield self.invoke(input)

def main():
    st.title("Sports-Arena")
    country = st.text_input("Enter your country:")
    if country:
        runnable = GreetingRunnable()
        response = runnable.invoke({"country": country})
        st.write(response)

if __name__ == "__main__":
    main()
