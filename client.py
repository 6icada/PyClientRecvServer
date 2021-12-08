# Code by 6icada
# Please do not copy code

# Tring to import libraries
try:
    import socket
except:
    # ERROR MSG
    print(f'[ERROR]: Can\'t import libraries...')

# Connect function
def Connect():
    # Adding vars
    HOST = input('Enter IPv4 address: ')
    PORT = 4444
    
    # Connecting to the server
    try:
        Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Client_Socket.connect((HOST, PORT))
    except:
        # ERROR MSG
        print('[ERROR]: Can\'t find server...')
        exit()

    # Closing connection
    Client_Socket.close()
    exit()

# Calling functions
Connect()
