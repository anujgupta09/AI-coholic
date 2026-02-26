import openai

from openai import OpenAI

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = openai.chat.completions.create(
    model="llama3.2:latest",
    messages=[{"role": "user", "content": "till what date you have info about?"}]
)
print(response.choices[0].message.content)
