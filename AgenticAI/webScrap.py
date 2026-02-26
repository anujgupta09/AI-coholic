from bs4 import BeautifulSoup
import requests

url = "https://www.thecreator.one/"

response = requests.get(url)

body=response.content

soup = BeautifulSoup(body, 'html.parser')

# print(soup.title.string)

content=soup.body.get_text(separator="\n",strip=True)
print(content)
# from openai import OpenAI

# openai=OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# response = openai.chat.completions.create(
#     model="gemma3:4b",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant who summarizes the content of the website."}, 
#         {"role": "user", "content": f"Take this content for summarizing: {content}"}
#     ]
# )
# print(response.choices[0].message.content)
