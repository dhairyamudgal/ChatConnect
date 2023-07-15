from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 512

# GLOBAL VARIABLES
messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

def recieve_messages():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode()
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]", e)
            break


def send_message(msg):
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


receive_thread = Thread(target=recieve_messages)
receive_thread.start()


send_message("Dhairya")
send_message("BROOO")