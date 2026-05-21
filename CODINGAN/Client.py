    import socket

    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Terhubung ke server.")

    while True:
        kata = input("Masukkan istilah jaringan (atau 'exit'): ")

        client_socket.send(kata.encode())

        if kata.lower() == "exit":
            break

        response = client_socket.recv(1024).decode()
        print("Hasil:", response)

    client_socket.close()