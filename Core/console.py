
def runConsole(running):
    while running:
        command=input()
        if command=="stop":
            print("[SERVER] Stopping server...")
            running=False
        else:
            print("[ERROR] Invalid Command")