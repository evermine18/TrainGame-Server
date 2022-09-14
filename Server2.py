import socket 
import threading
import Core.console, Core.connection, Core.serverManager

HEADER = 2
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="00"
connections=[]
sManager= Core.serverManager.ServerMagager(connections)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[SERVER] {addr} connected.")
    #Adds user to Users Dict
    connected = True
    while connected:
        data_id = conn.recv(HEADER).decode(FORMAT)
        if data_id:
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

def prueba():
    print("Hola")
        

def start():
    server.listen()
    print(f"[SERVER] Server is listening on {SERVER}")
    sConsole = threading.Thread(target=Core.console.runConsole, args=(sManager,))
    sConsole.start()
    
    while sManager.isRunning():
        #Accepting the connection
        conn, addr = server.accept()
        #Adding the new connection to a list
        connections.append(Core.connection.ClientThread(conn,addr,sManager))
        connections[len(connections)-1].start()
        
        print(f"[INFO] New user, Users Online: {threading.active_count() - 1}")


print("[SERVER] server is starting...")
start()