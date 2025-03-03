from openai import OpenAI

from ai.deepseek.Constant import api_key

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/beta",
)

messages = [
    {"role": "user", "content": "请写一个快速排序代码"},
    {"role": "assistant", "content": "```Java\n", "prefix": True}
]
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    stop=["```"],
)
print(response.choices[0].message.content)
