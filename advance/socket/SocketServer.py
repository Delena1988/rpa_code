# 服务器端
import socket

# 创建一个服务器Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定主机和端口
server_socket.bind(("localhost", 12345))

# 开始侦听
server_socket.listen(1)

# 接受连接
client_socket, client_address = server_socket.accept()
print(f"连接来自：{client_address}")

# 发送数据
client_socket.send(b"Hello, client!")

# 关闭连接
client_socket.close()
server_socket.close()
