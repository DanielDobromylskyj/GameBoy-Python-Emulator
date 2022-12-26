from emulator import OPCODES, RAM, ROM, CPU, Binary, ALU

import gui



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

    def LoadTXT(self, path):
        self.ROM.LoadTXT(path)


    def Execute(self):
        cpu = CPU.Main(self.RAM, self.ROM, self.Opcode, self.CMD, self.BIN, self.ALU)
        gui.Boot(cpu)

        cpu.Start_Executing_From_ROM()



def Main_Func():
    main = Main()

    main.LoadGB("tetris.gb")
    #main.LoadTXT("test.txt")
    main.Execute()






if __name__ == "__main__":
    #Testing_Main()
    Main_Func()