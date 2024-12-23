# 客户端
import socket

# 创建一个客户端Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect(("localhost", 12345))

# 发送
client_socket.send(b"111")
# 接受
data = client_socket.recv(1024)
print(data.decode("utf-8"))

client_socket.close()