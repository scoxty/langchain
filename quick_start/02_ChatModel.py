import os
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model=os.environ.get("LLM_MODEL_ENDPOINT"),
    messages=[
        {"role": "system", "content": "You are a creative AI."},
        {"role": "user", "content": "请给我的花店起个名"},
    ],
    temperature=0.8,
    max_tokens=600,
)

print(response.choices[0].message.content)