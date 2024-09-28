import os

import streamlit as st 
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

st.set_page_config(
    page_title="Chat with Gemini-Pro",
    page_icon="brain",
    layout="centered",
)

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel("gemini-pro")

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assisstant"
    else:
        return user_role
    
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("GeminiPro- ChatBot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
         st.markdown(message.parts[0].text)
        
user_p=st.chat_input("Ask Gemini Pro")

if user_p:
    st.chat_message("user").markdown(user_p)
    
    gemini_response=st.session_state.chat_session.send_message(user_p)
    
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
