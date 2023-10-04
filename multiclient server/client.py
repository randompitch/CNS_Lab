import socket

HEADER = 64
PORT = 5050
DISCONNECT_MSG = "!end"
SERVER = "192.168.29.224"
ADDR = (SERVER, PORT)

client = socket.socket()
client.connect(ADDR)

connected = True
while connected:
    msg = input("[CLIENT]: ")
    if msg == DISCONNECT_MSG:
        connected = False
        client.close()
    client.send(msg.encode())
    msg = client.recv(64).decode()
    if msg == DISCONNECT_MSG:
        connected = False
        client.close()
    print(f"[SERVER]: {msg}")

