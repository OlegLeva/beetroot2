import socket

IP = '127.0.0.1'
PORT = 54321

sock = socket.socket()
sock.bind((IP, PORT))
sock.listen()

while True:
    connection, addr = sock.accept()

    data = connection.recv(128)
    if not data:
        break

    connection.send(data.upper())


connection.close()

