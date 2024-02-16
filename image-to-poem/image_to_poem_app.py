'''app.py'''

import google.generativeai as genai
import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
visionModel = genai.GenerativeModel('gemini-pro-vision')

def geminiResponse(prompt, image):
    response = visionModel.generate_content([prompt, image])
    return response.text

st.title('''Image To Poem Generator
by: KVS Setty, AI Educator@DTC Infotech''')
imageUploaded = st.file_uploader("Upload image to generate a poem based on your uploaded image...")
#image = '' 

if imageUploaded is not None:
    image = Image.open(imageUploaded)
    st.image(image,caption="Image for which to generate a poem",use_column_width=True)
generate = st.button("Generate Poem")

prompt1 = '''You a veteran  poet. I will upload an image 
and based on the uploaded imge, you have to generate a poem in English'''

prompt2 = '''You are an experienced, world class poet. 
I will upload an image and based on the uploaded imge, 
you have to generate a poem.'''

if generate:
    response = geminiResponse(image,prompt2)
    st.write(response)