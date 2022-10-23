import socket
import threading
import constants as const
import pickle

class UDPServerSocket(object):
    def __init__(self):
        self.port = const.PROT
        self.host = const.HOST
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))

    def reseive(self):
        while True:
            try:
                data, addr = self.client_socket.recvfrom(1084)
                print(f"--> Server --> {data.decode()}")
            except:
                pass

    def start(self):
        print(f"[CONNECTION] Server is connected")
        while True:
            my_input = input("input: ")
            # self.server_socket.sendto(my_input.encode(), (self.host, const.PROT_CLIENT_A))
            self.server_socket.sendto(my_input.encode(), (self.host, const.PROT_CLIENT_B))



udp_server_socket = UDPServerSocket()
print("[STARTING] server is starting...")
udp_server_socket.start()