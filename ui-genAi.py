import streamlit as st
from genAISql import getQueryResult

st.title("Welcome to Natural Query Bot 🤖")
question= st.text_input(label="Ask Query",placeholder="Please enter your query here....")


if question:
    result=getQueryResult(question)
    st.header("Answer:")
    st.write(result)
