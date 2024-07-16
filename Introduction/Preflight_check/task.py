import socket


def port_available(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)
    try:
        print(f"Checking port {port}... ", end="")
        server_socket.bind(server_address)
        server_socket.listen(1)
    except OSError as e:
        print(f"FAILED: {e}")
        return False
    finally:
        server_socket.close()
    print("SUCCESS")
    return True


if __name__ == '__main__':
    port_available(5000)
    port_available(5001)
