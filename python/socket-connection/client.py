import socket

from constants import NUM_BYTES, pad_message

class Client:
    """Client that connects to the server, sends messages and receives an ACK."""

    def __init__(self, server_ip: str, server_port: int = 5000):
        self.server_ip: str = server_ip
        self.server_port: int = server_port

    def send_message(self, message: str | bytes):
        """Method to connect to the server and send a message.

        Args:
            message (str | bytes): Message to be sent.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.server_ip, self.server_port))  # Establish connection

            sock.send(pad_message(message))  # Send message

            message = sock.recv(NUM_BYTES)  # Receive ACK
            print(message)

if __name__ == "__main__":
    client = Client(server_ip="192.168.29.31")
    client.send_message("Hello, server!")
    client.send_message("How are you doing?")
    for msg in ["1", "2", "3"]:
        client.send_message(msg)
