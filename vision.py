from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

import streamlit as st
import os
from google import genai
from PIL import Image

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Gemini models and get response

def get_gemini_response(prompt,image):
    if prompt != "":
        response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[prompt, image]
    )
    else:
            response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[image]
        )
    return response.text

# Streamlit app
st.set_page_config(page_title="Gemini Image APP", page_icon="🤖")
st.header("Gemini Image APP")
input=st.text_input("Input: ",key="input")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
     image = Image.open(uploaded_file)
     st.image(image, caption='Uploaded Image.')
submit=st.button("Ask the Question")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("Response: ")
    st.write(response)