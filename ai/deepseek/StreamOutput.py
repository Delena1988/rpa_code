from openai import OpenAI
from Constant import api_key

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个知识渊博的助手，请帮助用户回答问题"},
        {"role": "user", "content": "预测一下奶茶行业的发展趋势"},
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='', flush=True)
