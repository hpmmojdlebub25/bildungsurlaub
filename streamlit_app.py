# %% packages
import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load Groq API key from Streamlit secrets and set as environment variable
if "groq" in st.secrets and "api_key" in st.secrets["groq"]:
    groq_api_key = st.secrets["groq"]["api_key"]
    os.environ["GROQ_API_KEY"] = groq_api_key
else:
    st.error("Groq API key not found in Streamlit secrets. Please set it in .streamlit/secrets.toml or Streamlit Cloud secrets.")
    st.stop()


model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

st.title("Unser erster Chatbot")
user_input = st.text_input("Gib hier deine Frage ein")
if user_input is not None:
    messages = [
        ("system", "Du bist ein Katze und kannst nur mit Katzensprache antworten."),
        ("user", user_input)
    ]
    prompt_template = ChatPromptTemplate.from_messages(messages)
    chain = prompt_template | model | StrOutputParser()
    response = chain.invoke({"topic": user_input})
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)

# %%





