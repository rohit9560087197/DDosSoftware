import threading
from gui import start_gui
from ddos_logic.packets import PacketHandler
import socket
import time

DEFAULT_BYTE_SIZE = 10000
DEFAULT_SERVER_BYTE_SIZE = 10000

def log_data(source, data):
    print(f"\033[31m{source}: ", end='')
    print(' '.join(str(b) for b in data))
    print("\033[37m")

def handle_client(client_socket, server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.connect((server_ip, server_port))
            print("Connected to server:", server_ip, server_port)
            
            while True:
                # Handle client to server communication
                client_data = client_socket.recv(DEFAULT_BYTE_SIZE)
                if client_data:
                    server_socket.sendall(client_data)
                    log_data("CLIENT", client_data)
                
                # Handle server to client communication
                server_data = server_socket.recv(DEFAULT_SERVER_BYTE_SIZE)
                if server_data:
                    client_socket.sendall(server_data)
                    log_data("SERVER", server_data)
                
                time.sleep(0.2)

    except Exception as e:
        print(f"An error occurred: {e}")

def proxy_start():
    server_ip = input("Type IP: ").strip()
    if not server_ip:
        server_ip = "127.0.0.1"
    
    port_str = input("Type PORT: ").strip()
    if not port_str:
        server_port = 25565
    else:
        server_port = int(port_str)
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
            proxy_socket.bind(('0.0.0.0', 5000))
            proxy_socket.listen(5)
            print("Proxy is started on port 5000!")
            
            while True:
                client_socket, addr = proxy_socket.accept()
                print("Accepted connection from:", addr)
                
                client_handler = threading.Thread(
                    target=handle_client, 
                    args=(client_socket, server_ip, server_port)
                )
                client_handler.start()
                
    except Exception as e:
        print(f"An error occurred: {e}")

