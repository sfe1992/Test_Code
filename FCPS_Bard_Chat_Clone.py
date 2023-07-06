from bardapi import Bard
import streamlit as st
from streamlit_chat import message
from PIL import Image
import os

os.environ["_BARD_API_KEY"] = "YAhqUhNAoFp4gjK4LOxyXktPDOiLRQNV43fb0u3XW8XietLvkJbdVvj7ULCu3d0dPZ4-mA."
default_prompt = 'You are a helpdesk staff member at Fairfax County Public School. Your answers to the following questions should be based solely on information about Fairfax County Public School located in Virginia, USA. If a question is not related to Fairfax County Public School, politely decline to answer. Never mention about "best regards" or similar greeting in your answer. Deny an answer for any topic related with the performance or the ranking. Deny an answer for generating a code (i.e. python, c++, c, java, html, basic, etc) and calculating math problems. Omit [Your name] in your answer. The content of the questions you are asking is as follows.'

st.set_page_config(
    page_title="Fairfax County Public Schools",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded"
)

image_contents = Image.open("FCPS_Brand.png")
st.image(image_contents, width=400)
st.subheader("Powered by Google Bard")

###Obtain the answer for the requested question
def response_api(promot):
    message=Bard().get_answer(str(promot))['content']
    return message


####Ask a question
def user_input(default_prompt):
    
    input_text=st.text_input("Question/Request:")
    return (default_prompt + '"' + input_text+'"')

if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

user_text = user_input(default_prompt)

if user_text != default_prompt + '""':
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text.replace(default_prompt + '"', '').replace('"', ''))

if st.session_state['generate']:
    for i in range(len(st.session_state['generate'])-1,-1,-1):
        message(st.session_state['past'][i], is_user = True, key = str(i)+'_user')
        message(st.session_state['generate'][i], key=str(i))