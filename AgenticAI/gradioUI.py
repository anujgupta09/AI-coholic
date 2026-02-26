
import os

from  dotenv import load_dotenv
load_dotenv()

#gemini -------------------------------------------------------

from google import genai
api_key = os.getenv("gemini")
client = genai.Client(api_key=api_key)

def gemini(prompt):
    gemini_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return gemini_response.text

#--------------------------------------------------------

import gradio

# from gradio import Interface

gradio.Interface(
    fn=gemini,
    inputs="text",
    outputs="text",
    title="ANUJ GUPTA CHAT APP",
).launch()
