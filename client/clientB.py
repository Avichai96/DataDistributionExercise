import socket
import threading
import constants as const

class UDPClientBSocket(object):
    def __init__(self):
        self.port = const.PROT_CLIENT_B
        self.host = const.HOST
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.bind((self.host, self.port))

    def reseive(self):
        print(f"[LISTENING] Server is listening on {self.host}")
        while True:
            try:
                data, addr = self.client_socket.recvfrom(1084)
                print(f"--> Client B --> {data.decode()}")
            except:
                pass


udp_client_socket = UDPClientBSocket()
print("[STARTING] server is starting...")
udp_client_socket.reseive()