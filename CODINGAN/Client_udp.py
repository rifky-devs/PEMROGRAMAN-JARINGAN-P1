import socket

# Membuat soket client dengan protokol UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello, UDP Server!"

# Langsung membungkus pesan dan melemparnya ke localhost port 9001
client_socket.sendto(message.encode("utf-8"), ('localhost', 9001))

# Menunggu dan menangkap balasan dari server
data, address = client_socket.recvfrom(1024)
print(data.decode("utf-8"))