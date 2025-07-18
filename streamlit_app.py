# %% packages
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True))
#from langchain_community.chat_models import ChatGroq


model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")


st.title("Unser erster Chatbot")
user_input = st.text_input("Gib hier deine Frage ein")
if user_input is not None:
    messages = [
        ("system", "Du bist ein Assistent, der hilft, Fragen zu beantworten."),
        ("user", user_input)
    ]
    prompt_template = ChatPromptTemplate.from_messages(messages)
    chain = prompt_template | model | StrOutputParser()
    response = chain.invoke({"topic": user_input})
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)

# %%





