import socket


if __name__ == '__main--':
    ip = '127.0.0.1'
    port = 8000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f'Connection Established - {address[0]}:{address[1]}')

        string = client.recv(1024)
        string = string.decode('utf-8')
        print(string)

        client.close()
