import os

from  dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI(
    api_key="os.getenv("openai")"
)

#print(client.chat.completions.list())

client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of Mumbai?"}
    ]
)