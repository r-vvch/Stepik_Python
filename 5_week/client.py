import time
import socket


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.client_socket = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError(err)

    def put(self, metric_name, load, timestamp=None):
        timestamp = str(timestamp or int(time.time()))
        data = 'put ' + str(metric_name) + ' ' + str(load) + ' ' + str(timestamp) + '\n'
        try:
            self.client_socket.send(data.encode())
            response = self.client_socket.recv(1024)
            if b'ok\n' not in response:
                raise ClientError
        except Exception:
            raise ClientError

    def get(self, metric_name):
        try:
            self.client_socket.send(('get ' + metric_name + '\n').encode("utf8"))
            data_string = self.client_socket.recv(1024).decode("utf8")
            strings = data_string.splitlines()

            if strings[0] != 'ok':
                raise ClientError

            output = {}
            for i in range(1, len(strings)):
                if len(strings[i]) > 0:
                    words = strings[i].split()
                    if words[0] in output.keys():
                        output[words[0]].append((int(words[2]), float(words[1])))
                        output.update({words[0]: sorted(output[words[0]])})
                    else:
                        output[words[0]] = [(int(words[2]), float(words[1]))]
            return output

        except Exception:
            raise ClientError
