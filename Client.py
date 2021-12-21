import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 5480
ADDR = (IP, PORT)
TEXT_MAXIMUM_SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "EXIT"
CONN_ACCEPTED_MESSAGE = "[SERVER] Connection accepted. Welcome!"
CONN_FAILED_MESSAGE = "[SERVER] Connection failed! Server is full. Try again later."
connected = False


def game_over(message):
    if message.find('You win!') != -1:
        return True
    if message.find('You lose!') != -1:
        return True
    return False


def client():
    global connected
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(ADDR)
    resultMsg = cli.recv(TEXT_MAXIMUM_SIZE).decode(FORMAT)
    if resultMsg == CONN_ACCEPTED_MESSAGE:
        print(CONN_ACCEPTED_MESSAGE)
        connected = True
    else:
        print(resultMsg)
    while connected:
        msg = input("[CLIENT]:")

        cli.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = cli.recv(TEXT_MAXIMUM_SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")
            if game_over(msg):
                connected = False


if __name__ == "__main__":
    client()
