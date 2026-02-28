import os
from huggingface_hub import InferenceClient

from dotenv import load_dotenv
load_dotenv()

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="Qwen/Qwen3.5-35B-A3B:novita",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image in one sentence."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
                    }
                }
            ]
        }
    ],
)

print(completion.choices[0].message.content)  