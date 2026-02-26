
# session 5.0
# learned about stream history and yield
# created kind of personal chatgpt 1st with gemini 2.5 flash and then with ollama gemma3:4b
# finally integrating with gradio UI 

import os
from  dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# openai = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=os.getenv("gemini"))
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

#-------------------------------------------------

# chat 

def anujChat(prompt, history):
    
    openai_response = openai.chat.completions.create(
        # model="gemini-2.5-flash",
        model = "gemma3:4b",
        messages=[{"role": "system", "content": "Always ans in least possible words without loosing info."}] + history + [{"role": "user", "content": prompt}],
        stream=True
    )

    res = ''
    for chunk in openai_response:
        res += chunk.choices[0].delta.content or ''
        yield(res)

#-------------------------------------------------

import gradio

gradio.ChatInterface(
    fn=anujChat,
    title="ANUJ GUPTA CHAT APP",
).launch()