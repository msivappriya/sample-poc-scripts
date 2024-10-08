import socket

from constants import NUM_BYTES, pad_message


class Server:
    """Server that accepts connection from a client, receives a message and sends an ACK."""
    def __init__(self, port: int = 5000):
        self.ip: str = socket.gethostbyname(socket.gethostname())
        self.port: int = port

    def run(self):
        """Method to begin the server application."""
        message: str = f"Server running on {self.ip}:{self.port}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.ip, self.port))
            sock.settimeout(1)  # Allow the server to handle interrupts at the end of the period.
            sock.listen()

            counter = 0
            print(message)
            while True:  # Keep running the server
                try:
                    conn, addr = sock.accept()  # Receive a connection
                    print(addr)
                    self.__handle(conn)
                except TimeoutError:  # Ignore timeouts
                    counter += 1
                    if counter % 10 == 0:
                        print(message)
                except KeyboardInterrupt:  # Stop the server on interrupt
                    print("Stopping server.")
                    break

    def __handle(self, conn: socket.socket):
        """Method to handle a connection from a client.

        Args:
            conn (socket.socket): Client connection.
        """
        message = conn.recv(NUM_BYTES)  # Receive a message
        print(message)

        conn.send(pad_message("Message received."))  # Send ACK

        conn.shutdown(socket.SHUT_RDWR)  # Shut down connection 
        conn.close()  # close connection


if __name__ == "__main__":
    server = Server()
    server.run()
