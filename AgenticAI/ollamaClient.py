import ollama

response = ollama.chat(
    model="gemma3:4b",
    messages=[{"role": "user", "content": "who is Anuj Gupta from Lineupx?"}]
)

print(response)