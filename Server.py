import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 5480
ADDR = (IP, PORT)
TEXT_MAXIMUM_SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "EXIT"
CONN_ACCEPTED_MESSAGE = "[SERVER] Connection accepted. Welcome!"
CONN_FAILED_MESSAGE = "[SERVER] Connection failed! Server is full. Try again later."
MAXIMUM_CONNECTIONS = 3
CURR_CONNECTIONS = 0


def server():
    print("[SERVER] Starting...")
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(ADDR)
    serv.listen()
    print(f"[SERVER] Server is listening on {IP}:{PORT}")
    global CURR_CONNECTIONS
    while True:
        if CURR_CONNECTIONS < MAXIMUM_CONNECTIONS:
            conn, addr = serv.accept()
            CURR_CONNECTIONS = CURR_CONNECTIONS + 1
            print(f"[SERVER] Active connections: {CURR_CONNECTIONS}")
            conn.send(CONN_ACCEPTED_MESSAGE.encode(FORMAT))
            if CURR_CONNECTIONS == MAXIMUM_CONNECTIONS:
                print("[SERVER] Maximum connections achieved")
        else:
            conn, addr = serv.accept()
            conn.send(CONN_FAILED_MESSAGE.encode(FORMAT))
            conn.close()


if __name__ == "__main__":
    server()
