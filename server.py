import socket


server = socket.create_server(('127.0.0.1', 8000))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.listen(10)

client_socket, address = server.accept()
received_date = client_socket.recv(1024).decode('utf-8 ')

print(f'Got data by socket {received_date}')