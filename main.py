from emulator import OPCODES, RAM, ROM, CPU, Binary, ALU



class Main:
    def __init__(self):
        self.RAM = RAM
        self.ROM = ROM.Cartridge()
        self.ALU = ALU

        self.Opcode = OPCODES.Codes()

        self.BIN = Binary
        self.CMD = ""

    def LoadGB(self, path):
        self.ROM.LoadGB(path)


    def Execute(self):
        cpu = CPU.Main(self.RAM, self.ROM, self.Opcode, self.CMD, self.BIN, self.ALU)
        cpu.Start_Executing_From_ROM()



def Main_Func():
    main = Main()

    main.LoadGB("tetris.gb")
    main.Execute()






if __name__ == "__main__":
    #Testing_Main()
    Main_Func()