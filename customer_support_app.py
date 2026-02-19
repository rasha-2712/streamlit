import streamlit as st
import os
from mistralai import Mistral, UserMessage

os.environ["MISTRAL_API_KEY"] = "YOUR_API_KEY_HERE"
api_key = os.getenv("MISTRAL_API_KEY")

def mistral_chat(user_message):
    client = Mistral(api_key=api_key)
    messages = [UserMessage(content=user_message)]
    response = client.chat.complete(
        model="mistral-large-latest",
        messages=messages,
    )
    return response.choices[0].message.content

st.title("Customer Support Chatbot")

user_input = st.text_input("Enter your question:")

if st.button("Send"):
    response = mistral_chat(user_input)
    st.write(response)