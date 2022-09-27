import asyncio

storage = {}


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())


def process_data(data):
    words = data.strip().split(' ')

    if words[0] == 'get':
        if len(words) == 2:
            output = 'ok\n'
            if words[1] == '*':
                for key, value_list in storage.items():
                    for params in value_list:
                        output += f'{key} {params[1]} {params[0]}\n'
            elif words[1] in storage:
                for value in storage[words[1]]:
                    output += f'{words[1]} {value[1]} {value[0]}\n'
            output += '\n'
            return output
        return "error\nwrong command\n\n"

    elif words[0] == 'put':
        if len(words) == 4:
            output = "ok\n\n"
            try:
                key, value, time = words[1], float(words[2]), int(words[3])
            except ValueError:
                return "error\nwrong command\n\n"
            if key in storage:
                old_data = storage[key]
                for metric_values in old_data:
                    if metric_values[0] == time:
                        old_data.remove((metric_values[0], metric_values[1]))
                        break
                old_data.append((time, value))
                storage.update({key: sorted(storage[key])})
            else:
                storage[key] = [(time, value)]
            return output
        return "error\nwrong command\n\n"

    else:
        return 'error\nwrong command\n\n'


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
