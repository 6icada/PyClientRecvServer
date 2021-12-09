# Code by 6icada
# Please do not copy code

# Tring to import libraries
try:
    import socket
except:
    # ERROR MSG
    print(f'[ERROR]: Can not import libraries...')
    exit()

# MakeSocket function
def MakeSocket():
    # Adding vars
    HOST = '0.0.0.0'
    PORT = 4444
    clients = []

    # Binding Server
    Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server_Socket.bind((HOST, PORT))
    Server_Socket.listen()

    # MSG when server starts
    print(f'[START]: Server started on {HOST}:{PORT}')

    # Handle function
    def Handle():
        while True:
            # Adding vars
            client, address = Server_Socket.accept()

            # Adding address(client's address) to clients list
            clients.append(address)

            # MSG when client joins
            print(f'[CLIENT]: {address} connected to the server!')

    # Calling functions
    Handle()

# Calling functions
MakeSocket()

