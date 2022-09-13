class ServerMagager():
    
    def __init__(self):
        self.Running=True
        self.Users = {}
        self.UId = 0

    def newUser(self):
        self.Users[self.UId]=[0,0]
        self.UId+=1
    
    def isRunning(self):
        return self.Running
    
    def getUId(self):
        return self.UId

    def stopServer(self):
        self.Running=False

    def getUsers(self):
        return self.Users