import socket
import threading

PORT = 55555
SERVER = '172.21.144.1'

clients = []
u_names = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            u_name = u_names[index]
            broadcast(f"{u_name} left the chat.".encode('ascii'))
            u_names.remove(u_name)
            break


def receive():
    server.listen()
    print(f"[LISTENING] Server is Listening on {SERVER}")
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send('USER NAME'.encode('ascii'))
        u_name = client.recv(1024).decode('ascii')
        u_names.append(u_name)
        clients.append(client)

        print(f'nickname of the client is {u_name}')
        broadcast(f"{u_name} joined the chat!".encode('ascii'))
        client.send("Connected to the chat!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("[STARTING] Server is Starting...")
receive()
