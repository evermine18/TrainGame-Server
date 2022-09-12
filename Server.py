import socket 
import threading

HEADER = 2
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
Users = {}
UId = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    global Users, UId
    print(f"[SERVER] {addr} connected.")
    #Adds user to Users Dict
    Users[UId]=[0,0]
    UId+=1
    print(UId)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            
            print(msg_length)
            """
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
            """
    conn.close()
        

def start():
    server.listen()
    print(f"[SERVER] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[SERVER] {threading.active_count() - 1}")


print("[SERVER] server is starting...")
start()