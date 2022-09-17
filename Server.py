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
  

def start():
    server.listen()
    print(f"[SERVER] Server is listening on {SERVER}")
    #Starting the console to get user commands
    sConsole = threading.Thread(target=Core.console.runConsole, args=(sManager,))
    sConsole.start()

    while sManager.isRunning():
        #Accepting the connection
        conn, addr = server.accept()
        #Adding the new connection to a list
        connections.append(Core.connection.ClientThread(conn,addr,sManager))
        connections[len(connections)-1].start()
        
        print(f"[INFO] New user, Users Online: {len(connections)}")


print("[SERVER] server is starting...")
start()