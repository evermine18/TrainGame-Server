
def runConsole(sManager):
    while sManager.isRunning():
        command=input()
        if command=="stop":
            print("[SERVER] Stopping server...")
            sManager.stopServer()
        else:
            print("[ERROR] Invalid Command")