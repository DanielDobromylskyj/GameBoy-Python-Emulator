

class Cartridge():
    def __init__(self):
        self.RawGB = []
        self.FileSize = 0

    def LoadGB(self, path): # Reads data from a .asm file (e.g. tetris.asm)
        f = open(path, "rb")
        data = f.read().hex()
        f.close()


        self.RawGB = [data[i*2:(i*2)+2] for i in range(len(data) // 2)]
        self.FileSize = len(self.RawGB)

    def LoadTXT(self, path):
        f = open(path, "r")
        data = f.read()
        f.close()

        data = data.replace("\n", "").replace(" ", "")

        self.RawGB = [data[i*2:(i*2)+2] for i in range(len(data) // 2)]
        self.FileSize = len(self.RawGB)


    def Read(self, Location):
        if int(Location) < self.FileSize:
            return self.RawGB[int(Location)]
        print("[Emulator][ROM] Cannot Read Value", Location, "It does not exist")


class Built_in():
    def __init__(self):
        self.RawGB = []
        self.FileSize = 0
        self.LoadGB()

    def LoadGB(self, path): # Reads data from a .asm file (e.g. tetris.asm)
        f = open(path, "rb")
        data = f.read().hex()
        f.close()


        self.RawGB = [data[i*2:(i*2)+2] for i in range(len(data) // 2)]
        self.FileSize = len(self.RawGB)



    def Read(self, Location):
        if int(Location) < self.FileSize:
            return self.RawGB[int(Location)]
        print("[Emulator][ROM] Cannot Read Value", Location, "It does not exist")