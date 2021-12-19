import socket

HOST = "127.0.0.1"
PORT = 32017
MAX_CLIENTS = 2


class ThreadedServer(object):
    maximumNoClientsMessagePrinted = False

    def __init__(self, host, port, maxClients):
        self.host = host
        self.port = port
        self.maxClients = maxClients
        self.connected_clients = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.maximumNoClientsMessagePrinted = False

    def listen(self):
        self.sock.listen()

        while True:

            if self.maximumNoClientsMessagePrinted is False and self.connected_clients >= self.maxClients:
                print("Maximum number of clients reached")
                self.maximumNoClientsMessagePrinted = True
                continue
            if self.connected_clients < self.maxClients:
                client, address = self.sock.accept()
                # keep track connected clients
                self.connected_clients += 1

            # start a new thread to send data to the connected client
            # start a new thread to receive data to the connected client


if __name__ == "__main__":
    ThreadedServer(HOST, PORT, MAX_CLIENTS).listen()
