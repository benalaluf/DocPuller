import struct


class Protocol:
    def __init__(self, server, port):
        self.SERVER = server
        self.PORT = port
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MSG = 'EXIT'

    def recv_file(self, sock):
        file_name = self.__recv_string(sock)
        file_data = self.__recv_data(sock)
        return file_name, file_data

    def send_file(self, sock, filename, filedata):
        self._send_string(sock, filename)
        self.__send_data(sock, filedata)

    def __send_data(self, sock, data):
        data = struct.pack('>Q', len(data)) + data
        sock.sendall(data)

    def _send_string(self, sock, data):
        data = struct.pack('>I', len(data)) + data
        sock.sendall(data)

    def __recv_data(self, sock):
        raw_data_len = self.__recvall(sock, 8)
        if not raw_data_len:
            return None
        data_len = struct.unpack('>Q', raw_data_len)[0]
        return self.__recvall(sock, data_len)

    def __recv_string(self, sock):
        raw_data_len = self.__recvall(sock, 4)
        if not raw_data_len:
            return None
        data_len = struct.unpack('>I', raw_data_len)[0]
        return self.__recvall(sock, data_len)

    def __recvall(self, sock, data_len):
        data = bytearray()
        while len(data) < data_len:
            packet = sock.recv(data_len - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data
