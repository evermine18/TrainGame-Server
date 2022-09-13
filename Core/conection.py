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
    self.id=sManager.getUId()
    sManager.newUser()

  def si():
    print ("si")
    
  def run(self):
    connected = True
    while connected:
        data_id = self.conn.recv(self.HEADER).decode(self.FORMAT)
        if data_id:
            print(data_id)
            if data_id==self.DISCONNECT_MESSAGE:
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
    print(f"[SERVER] Closing the conection {self.addr}")
    self.conn.close()