from emulator import OPCODES, RAM, ROM, CPU, Commands



class Main:
    def __init__(self):
        self.RAM = RAM
        self.ROM = ROM.ROM()

        self.Opcode = OPCODES.Codes()


        self.Registers = RAM.Register
        self.CMD = Commands

    def LoadGB(self, path):
        self.ROM.LoadGB(path)


    def Execute(self):
        cpu = CPU.Main(self.RAM, self.ROM, self.Opcode, self.CMD)
        cpu.Start_Executing_From_ROM()



def Main_Func():
    main = Main()

    main.LoadGB("tetris.gb")
    main.Execute()






if __name__ == "__main__":
    #Testing_Main()
    Main_Func()