import struct


class Protocol:
    def __init__(self, server, port):
        self.HEADER = 4
        self.SERVER = '192.168.1.133'
        self.PORT = 8082
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MSG = 'EXIT'

    def recv_file(self, sock):
        file_name = self.__recv_string(sock)
        file_data = self.__recv_data(sock)
        return file_name, file_data

    def send_file(self, sock, filename, filedata):
        self.__send_string(sock, filename)
        self.__send_data(sock, filedata)

    def __send_data(self, sock, data):
        data = struct.pack('>Q', len(data)) + data
        sock.sendall(data)

    def __send_string(self, sock, data):
        data = struct.pack('>I', len(data)) + data
        sock.sendall(data)

    def __recv_data(self, sock):
        raw_datalen = self.__recvall(sock, 8)
        if not raw_datalen:
            return None
        datalen = struct.unpack('>Q', raw_datalen)[0]
        return self.__recvall(sock, datalen)

    def __recv_string(self, sock):
        raw_datalen = self.__recvall(sock, 4)
        if not raw_datalen:
            return None
        datalen = struct.unpack('>I', raw_datalen)[0]
        return self.__recvall(sock, datalen)

    def __recvall(self, sock, data_len):
        data = bytearray()
        while len(data) < data_len:
            packet = sock.recv(data_len - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data
