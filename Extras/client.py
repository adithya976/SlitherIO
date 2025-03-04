import socket

PORT = 5050
SERVER = "172.21.144.1"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "DISCONNECT"
CLIENT = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)


while True:
    msg = input("\b")
    print(f"{CLIENT} MESSAGE: {msg}")

    send(msg)
