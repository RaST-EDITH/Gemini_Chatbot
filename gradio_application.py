# Chatbot using Gemini API
from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Funtion to load Gemini Pro model and get response

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question) :

    response = chat.send_message( question, stream=True)
    return response

# Implementing gradio method
iface = gr.Interface( fn=get_gemini_response, inputs=gr.components.Textbox(lines=7, label="Enter your text"),
                      outputs="text", title="Custom-trained Chatbot")

iface.launch(share=True)
