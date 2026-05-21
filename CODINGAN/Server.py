import socket

# Kamus istilah jaringan
kamus = {
    "TCP": "Protokol handal (reliable) dengan koneksi",
    "UDP": "Protokol tanpa koneksi (connectionless)",
    "IP": "Alamat unik untuk identifikasi perangkat di jaringan",
    "DNS": "Sistem penerjemah nama domain ke IP address",
    "HTTP": "Protokol untuk komunikasi web"
}

# Setup server
host = '127.0.0.1'
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server berjalan, menunggu koneksi...")

conn, addr = server_socket.accept()
print("Terhubung dengan:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    if data.lower() == "exit":
        print("Client keluar.")
        break

    # Cek di kamus
    response = kamus.get(data.upper(), "Maaf, kata tidak ditemukan")

    conn.send(response.encode())

conn.close()
server_socket.close()