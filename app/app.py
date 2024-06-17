#Import required packages

import streamlit as st
import requests
import os
import json

#Load env variables
BACKEND_IP = os.getenv('BACKEND_IP')
BACKEND_PORT = os.getenv('BACKEND_PORT')
BASE_URL = f'http://{BACKEND_IP}:{BACKEND_PORT}'


#function to call root api endpoint
def call_root_endpoint():
    result = requests.get(url=f'{BASE_URL}')
    result = result.json()
    msg = result.get('messsage')
    return msg
    

#Function to make api call to get uuid
def get_uuid():
    result = requests.get(url=f'{BASE_URL}/generate')
    result = result.json()
    uuid = result.get('uuid')
    return uuid

#Create streamlit app 

st.markdown(
    f'<div style="text-align: center;"><h1>UUID Generator</h1></div>', unsafe_allow_html=True
)

with st.container():
    if st.button('GENERATE',use_container_width=True):
        uuid = get_uuid()
        st.markdown(f'<div style="display: flex; justify-content: center; align-items: center; height: 30px; background-color: #10785c; padding: 5px; border-radius: 5px;"><p style="color: white; margin: 0;">{uuid}</p></div>', unsafe_allow_html=True)
        st.balloons()
with st.sidebar:
    if st.button('HELLO'):
        message = call_root_endpoint()
        st.write(message)

