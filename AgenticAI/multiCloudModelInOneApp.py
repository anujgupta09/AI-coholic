
import os

from  dotenv import load_dotenv
load_dotenv()

#gemini -------------------------------------------------------
from google import genai
api_key = os.getenv("gemini")
client = genai.Client(api_key=api_key)
gemini_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)
print(gemini_response)

#anthropic -----------------------------------------------------
import anthropic
api_key = os.getenv("anthropic")
anthropic_client = anthropic.Client(api_key=api_key)
anthropic_response = anthropic_client.completions.create(
    model="claude-sonnet-4",
    prompt="Hello",
    max_tokens_to_sample=100
    )
print(anthropic_response)
anthropic_response2=anthropic_client.messages.create(
    messages=[{ "role": "user", "content": "Hello, Claude" }],
    model="claude-sonnet-4",
    max_tokens=100
)
print(anthropic_response2)

#deepseek --------------------------------------------------------
from openai import OpenAI
openai = OpenAI(base_url="https://api.deepseek.com", api_key=os.getenv("deepseek"))

deepseek_response = openai.chat.completions.create(
    model="deepseek-2.0",
    messages=[
        {"role": "user", "content": "Hi , how are you ?"},
    ]
)

deepseek_response = openai
print(deepseek_response)