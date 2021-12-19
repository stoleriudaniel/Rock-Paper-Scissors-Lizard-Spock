import socket

HOST = "127.0.0.1"
PORT = 32017


class ThreadedClient(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self):
        self.sock.connect((self.host, self.port))

        # start a new thread to receive data to the server
        # start a new thread to send data to the server


if __name__ == "__main__":
    ThreadedClient(HOST, PORT).send()
