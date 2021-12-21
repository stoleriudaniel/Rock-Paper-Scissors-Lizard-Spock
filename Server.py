import socket
import threading
import random

IP = socket.gethostbyname(socket.gethostname())
PORT = 5480
ADDR = (IP, PORT)
TEXT_MAXIMUM_SIZE = 1024
FORMAT = "utf-8"
EXIT_MESSAGE = "EXIT"
CONN_ACCEPTED_MESSAGE = "[SERVER] Connection accepted. Welcome!"
CONN_FAILED_MESSAGE = "[SERVER] Connection failed! Server is full. Try again later."
MAXIMUM_CONNECTIONS = 3
CURR_CONNECTIONS = 0

possible_options = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]


def valid_option(option):
    return option in possible_options


def option1_bigger_than_option2(option1, option2):
    return [option1, option2] in [
        ["SCISSORS", "PAPER"],
        ["PAPER", "ROCK"],
        ["ROCK", "LIZARD"],
        ["LIZARD", "SPOCK"],
        ["SPOCK", "SCISSORS"],
        ["SCISSORS", "LIZARD"],
        ["LIZARD", "PAPER"],
        ["PAPER", "SPOCK"],
        ["SPOCK", "ROCK"]
    ]


def handle_client(conn, addr):
    global CURR_CONNECTIONS
    rounds = []
    connected = True
    while connected:
        client_option = conn.recv(TEXT_MAXIMUM_SIZE).decode(FORMAT)
        if client_option == EXIT_MESSAGE:
            connected = False
        elif valid_option(client_option) is False:
            message = "Your option is not valid!"
            conn.send(message.encode(FORMAT))
        elif valid_option(client_option) is True:
            message = "Your option is valid!"
            conn.send(message.encode(FORMAT))
            random_index = random.randint(0, 4)
            server_option = possible_options[random_index]

    conn.close()
    CURR_CONNECTIONS = CURR_CONNECTIONS - 1
    print(f"[SERVER] Active connections: {CURR_CONNECTIONS}")


def server():
    print("[SERVER] Starting...")
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(ADDR)
    serv.listen()
    print(f"[SERVER] Server is listening on {IP}:{PORT}")
    global CURR_CONNECTIONS
    while True:
        conn, addr = serv.accept()
        if CURR_CONNECTIONS < MAXIMUM_CONNECTIONS:
            CURR_CONNECTIONS = CURR_CONNECTIONS + 1
            print(f"[SERVER] Active connections: {CURR_CONNECTIONS}")
            conn.send(CONN_ACCEPTED_MESSAGE.encode(FORMAT))
            if CURR_CONNECTIONS == MAXIMUM_CONNECTIONS:
                print("[SERVER] Maximum connections achieved")
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
        else:
            conn.send(CONN_FAILED_MESSAGE.encode(FORMAT))
            conn.close()


if __name__ == "__main__":
    server()
