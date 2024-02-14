from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# now wee are writing function to load Gemini Pro mode land get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True) # as llm modelis giving u the output we will steam and show the output
    return response

# now we are gonna initialize our streamlit app
st.set_page_config(page_title='qna_on_chatbot_development')

st.header("Gemini LLM Application")

# Initialize session state for chat history if it does'nt exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input('Input:',key='input')  
submit=st.button("Ask the question") 

if submit and input:
    response=get_gemini_response(input)
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(('You',input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))

st.subheader("The Chat history is")
for role,text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')