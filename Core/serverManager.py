class ServerMagager():
    
    def __init__(self,connections):
        self.Running=True
        self.Users = {"23":[234,556]}
        self.UId = 0
        self.connections = connections
        print("1r ",connections)

    def newUser(self):
        if len(str(self.UId))==1:
            self.Users["0"+str(self.UId)]=[0,0]
        else:
            self.Users[str(self.UId)]=[0,0]
        self.UId+=1
    
    def disconnected(self,id):
        #Deleting user from Users list and notify to all connections this event
        self.Users.pop(id)
        for conn in self.connections:
            conn.disconnectedUser(id)

    def showConnections(self):
        print(self.connections)
    
    def isRunning(self):
        return self.Running
    
    def getUId(self):
        return self.UId

    def stopServer(self):
        self.Running=False

    def getUsers(self):
        return self.Users