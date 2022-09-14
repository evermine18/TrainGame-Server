
import socket
import threading

HEADER = 2
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "00"
SERVER = "192.168.1.45"
ADDR = (SERVER, PORT)

players={}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = msg
    send_length = str(msg_length).encode(FORMAT)
    #send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    #client.send(message)
    #print(client.recv(2048).decode(FORMAT))

def sendCords():
    while True:
        send_length = str("01").encode(FORMAT)
        client.send(send_length)
        xpos = str("123456").encode(FORMAT)
        client.send(xpos)
        ypos = str("654321").encode(FORMAT)
        client.send(ypos)
    #data = str("00").encode(FORMAT)
    #client.send(data)

def recive():
    while True:
        data_id=client.recv(HEADER).decode(FORMAT)
        print(data_id)
        if data_id:
            #Player data
            if data_id=="01":
                playerID=client.recv(2).decode(FORMAT)
                xpos=client.recv(6).decode(FORMAT)
                ypos=client.recv(6).decode(FORMAT)
                players[playerID]=[xpos,ypos]
                print(players)


def gameSim():
    while True:
        client.recv(2048).decode(FORMAT)

reciveData=threading.Thread(target=recive)
reciveData.start()
sendCords()
#send(DISCONNECT_MESSAGE)