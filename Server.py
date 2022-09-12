import socket 
import threading
import Core.console

HEADER = 2
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="00"
Running=True
Users = {}
UId = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    global Users, UId
    print(f"[SERVER] {addr} connected.")
    #Adds user to Users Dict
    Users[UId]=[0,0]
    ID=UId
    UId+=1
    connected = True
    while connected:
        data_id = conn.recv(HEADER).decode(FORMAT)
        if data_id:
            print(data_id)
            if data_id==DISCONNECT_MESSAGE:
                connected=False
            """
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
            """
    print(f"[SERVER] Closing the conection {addr}")
    conn.close()
        

def start():
    global Running
    server.listen()
    print(f"[SERVER] Server is listening on {SERVER}")
    sConsole = threading.Thread(target=Core.console.runConsole, args=(Running,))
    sConsole.start()
    while Running:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[SERVER] {threading.active_count() - 1}")


print("[SERVER] server is starting...")
start()