import socket
import threading


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(5)

print("服务器已启动，等待连接...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"接受来自 {addr[0]}:{addr[1]} 的连接")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
