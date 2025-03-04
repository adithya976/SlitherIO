import socket
import threading

u_name = input("Enter USERNAME: ")

CLIENT = socket.gethostbyname(socket.gethostname())
SERVER = '172.21.144.1'
port = 55555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'USER NAME':
                client.send(u_name.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        message = f'{u_name}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
