from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        response.resolve()  # Ensure the response is fully available
        
        # Inspect the response object to find the correct attribute
        # print(dir(response))  # For debugging: print available attributes
        
        # Assuming the correct attribute is 'text', adjust based on inspection
        return response.text  # Replace 'text' with the actual attribute found
        
    except genai.types.IncompleteIterationError as e:
        return f"Error: {str(e)}"
    except AttributeError as e:
        return f"AttributeError: {str(e)} - Please check the available attributes of the response object."

# Implementing Gradio method
iface = gr.Interface(
    fn=get_gemini_response,
    inputs=gr.components.Textbox(lines=7, label="Enter your text"),
    outputs="text",
    title="Custom-trained Chatbot"
)

iface.launch(share=True)
