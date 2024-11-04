import os
from openai import OpenAI

# 实际配置使用的是豆包模型
# 火山方舟大模型 / 智能体调用 v3 API 与 OpenAI API 协议兼容
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model=os.environ.get("LLM_MODEL_ENDPOINT"),
    messages=[
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "常见的十字花科植物有哪些？"},
    ],
)
print(completion.choices[0].message.content)

print()

# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model=os.environ.get("LLM_MODELEND"),
    messages=[
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "常见的十字花科植物有哪些？"},
    ],
    stream=True
)

for chunk in stream:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content, end="")
print()