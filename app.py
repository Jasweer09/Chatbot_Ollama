from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("You are helpful assistante. Please response to the user queries"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

st.title("ChatBot with Langchain and Ollama")
input_text = st.text_input("Search the topic u want")

llm = Ollama(model="gemma")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))