import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model=os.environ.get("LLM_MODEL_ENDPOINT"),
    temperature=0.8,
    max_tokens=600,
)
response = llm.invoke("请给我的花店取个名字")

print(response)