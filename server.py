import socket
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def close_socket():
    try:
        #  don't work on my macbook
        server.shutdown(socket.SHUT_RDWR)
    except OSError:
        pass
    server.close()
    logger.info('Server was closed')


if __name__ == '__main__':
    with open('index.html') as file:
        html = file.read()

    server = socket.create_server(('127.0.0.1', 8001))
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.listen(10)


    while True:
        try:
            client_socket, address = server.accept()
        except KeyboardInterrupt: # when user presed ctr + c
            close_socket()
            break
        received_date = client_socket.recv(1024).decode('utf-8 ')

        logger.info(f'Got data by socket {received_date}')
        path = received_date.split()[1]

        logger.info(f"Parsed {path=}")

        response = f'HTTP/1.1 200 OK\nContent-type: text/html; charset=utf-8\n\n{html}'
        client_socket.send(response.encode('utf-8'))
        client_socket.shutdown(socket.SHUT_RDWR)
