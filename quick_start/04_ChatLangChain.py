import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(
    model=os.environ.get("LLM_MODEL_ENDPOINT"),
    temperature=0.8,
    max_tokens=600,
)

messages = [
    SystemMessage(content="你是一个很棒的智能助手"),
    HumanMessage(content="请给我的花店起个名"),
]

response = chat.invoke(messages)
print(response)