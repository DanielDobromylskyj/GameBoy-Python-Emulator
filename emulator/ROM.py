

class ROM():
    def __init__(self):
        self.RawGB = []
        self.FileSize = 0

    def LoadGB(self, path): # Reads data from a .asm file (e.g. tetris.asm)
        f = open(path, "rb")
        data = f.read().hex()
        f.close()

        self.RawGB = [data[i*2:(i*2)+2] for i in range(len(data) // 2)]
        self.FileSize = len(self.RawGB)

    def Refortmat(self, Opcode, SavePath):



    def Read(self, Location):
        if int(Location) < self.FileSize:
            return self.RawGB[int(Location)]
        print("[Emulator][ROM] Cannot Read Value", Location, "It does not exist")