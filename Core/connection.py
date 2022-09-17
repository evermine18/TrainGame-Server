import threading
import time

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
    #Adding new user to severManager
    sManager.newUser()
    #Printing info for the development
    currentPos=threading.Thread(target=self.currentPos)
    currentPos.start()

  def disconnectedUser(self,id):
    self.pTasks.append(["disconnect",id])

  def currentPos(self):
    while True:
      print("User list: ",self.sManager.getUsers())
      time.sleep(3)

  def listen(self):
    while self.connected:
      #First this method identify the type of data that client are sending
      data_id = self.conn.recv(self.HEADER).decode(self.FORMAT)
      if data_id:
        #Disconnected user
        if data_id==self.DISCONNECT_MESSAGE:
          self.sManager.disconnected(self.id)
          self.connected=False
        #Player data like coords, username...
        elif(data_id=="01"):
          xpos = self.conn.recv(6).decode(self.FORMAT)
          ypos = self.conn.recv(6).decode(self.FORMAT)
          self.sManager.updateUser(self.id,xpos,ypos)

  def run(self):
    listen=threading.Thread(target=self.listen)
    listen.start()
    while True:
      #Sending all users pos
      for playerID in self.sManager.getUsers().keys():
        if playerID!=self.id:
          #Sending dataID
          self.conn.send("01".encode(self.FORMAT))
          #Sending a pos with 6 digits max
          xpos=str(self.sManager.getUsers()[playerID][0])
          xpos="0"*(6-len(xpos))+xpos
          ypos=str(self.sManager.getUsers()[playerID][1])
          ypos="0"*(6-len(ypos))+ypos
          self.conn.send(playerID.encode(self.FORMAT))
          self.conn.send(xpos.encode(self.FORMAT))
          self.conn.send(ypos.encode(self.FORMAT))

    print(f"[SERVER] Closing the conection {self.addr}")
    self.conn.close()
    