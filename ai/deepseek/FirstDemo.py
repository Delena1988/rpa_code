from openai import OpenAI
from Constant import api_key


client = OpenAI(api_key= api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好，请问你是谁？"},
    ],
    stream=False
)

print(response.choices[0].message.content)
