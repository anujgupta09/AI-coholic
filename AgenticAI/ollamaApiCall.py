ollama_api = "http://localhost:11434/api/chat"
header = {
    "Content-Type": "application/json"
}
model = "gemma3:4b"
prompt = "Hiii reply in 1 word"
message = [{ "role": "user", "content": prompt }]
payload = {
    "model": model,
    "messages": message
}
import requests
response = requests.post(ollama_api, json=payload, headers=header)
print(response.text)