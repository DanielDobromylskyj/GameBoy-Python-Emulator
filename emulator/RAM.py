


class RAM():
    def __init__(self): # Init
        self.Data = {}

    def Write(self, Pos, Data): # Write Data To POS
        self.Data[Pos] = Data

    def Read(self, Pos): # Read From Pos
        try:
            return self.Data[Pos]
        except:
            print("[Emulator][RAM] Read Error, No Data Set At Pos:", Pos)




class Register():
    def __init__(self, Data=None):
        if Data == None:
            self.Data = 0
        else:
            self.Data = Data

    def Fetch(self):
        return self.Data

    def Set(self, Data):
        self.Data = Data
