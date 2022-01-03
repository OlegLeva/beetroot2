import socket

IP = '127.0.0.1'
PORT = 54321
msg = 'hallo'
sock = socket.socket()
sock.connect((IP, PORT))

sock.sendall(bytes(msg, encoding='utf-8'))
data = sock.recv(128)
with open('text.txt', 'a') as f:
    print(data.decode(), file=f)

print()
sock.close()