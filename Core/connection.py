import re
import threading

class ClientThread(threading.Thread):
  # overriding constructor
  def __init__(self, conn, addr,sManager):
    # calling parent class constructor
    threading.Thread.__init__(self)
    self.conn=conn
    self.addr=addr
    self.HEADER = 2
    self.FORMAT = 'utf-8'
    self.DISCONNECT_MESSAGE="00"
    self.connected=True
    self.sManager=sManager
    self.pTasks=[]
    self.id=str(sManager.getUId())
    #Checking len
    if len(self.id)==1:
      #converting to 2 digits
      self.id="0"+self.id
    sManager.newUser()

  def disconnectedUser(self,id):
    self.pTasks.append(["disconnect",id])

  def listen(self):
    while self.connected:
      data_id = self.conn.recv(self.HEADER).decode(self.FORMAT)
      if data_id:
        if data_id==self.DISCONNECT_MESSAGE:
          self.sManager.disconnected(self.id)
          self.connected=False
        elif(data_id=="01"):
          print("Reciving pos")
          xpos = self.conn.recv(6).decode(self.FORMAT)
          ypos = self.conn.recv(6).decode(self.FORMAT)
          print("Recived Coords: ",xpos," ",ypos)
    
  def run(self):
    listen=threading.Thread(target=self.listen)
    listen.start()
    while True:
      for playerID in self.sManager.getUsers().keys():
        if playerID!=self.id:
          self.conn.send("01".encode(self.FORMAT))
          xpos=str(self.sManager.getUsers()[playerID][0])
          xpos="0"*(6-len(xpos))+xpos
          ypos=str(self.sManager.getUsers()[playerID][1])
          ypos="0"*(6-len(ypos))+ypos
          self.conn.send(playerID.encode(self.FORMAT))
          self.conn.send(xpos.encode(self.FORMAT))
          self.conn.send(ypos.encode(self.FORMAT))
      """
      if msg_length:
          msg_length = int(msg_length)
          msg = conn.recv(msg_length).decode(FORMAT)
          if msg == DISCONNECT_MESSAGE:
              connected = False

          print(f"[{addr}] {msg}")
          conn.send("Msg received".encode(FORMAT))
    """
    print(f"[SERVER] Closing the conection {self.addr}")
    self.conn.close()