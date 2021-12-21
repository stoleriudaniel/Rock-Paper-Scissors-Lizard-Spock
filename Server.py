import socket
import threading

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
rounds = []


def is_valid_option(option):
    return option in possible_options


def handle_client(conn, addr):
    global CURR_CONNECTIONS
    connected = True
    while connected:
        message = conn.recv(TEXT_MAXIMUM_SIZE).decode(FORMAT)
        if message == EXIT_MESSAGE:
            connected = False
        conn.send(message.encode(FORMAT))
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
