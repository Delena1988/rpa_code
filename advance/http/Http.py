import requests

print("=============Get=============")
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
# 打印状态码
print(response.status_code)
# 打印返回的JSON数据
print(response.json())

print("=============Post=============")
url = "https://jsonplaceholder.typicode.com/posts"
data = {'id': 1, 'title': 'updated title', 'body': 'updated body', 'userId': 1}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())

print("=============Put=============")
url = "https://jsonplaceholder.typicode.com/posts/1"
data = {'id': 1, 'title': 'updated title', 'body': 'updated body', 'userId': 1}
response = requests.put(url, json=data)
print(response.status_code)
print(response.json())

print("=============Put=============")
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)
print(response.status_code)

print("=============Header=============")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get('https://jsonplaceholder.typicode.com', headers=headers)

print("=============Error Handle=============")
try:
    response = requests.get('https://example.com/nonexistent_page')
    response.raise_for_status()  # 如果状态码不是200，则引发HTTPError异常
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)
