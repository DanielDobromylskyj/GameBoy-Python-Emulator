from emulator import OPCODES, RAM, ROM, CPU



class Main:
    def __init__(self):
        self.RAM = RAM.RAM()
        self.ROM = ROM.ROM()


        self.Opcode = OPCODES.Codes()


        self.Registers = RAM.Register

    def LoadGB(self, path):
        self.ROM.LoadGB(path)


    def Execute(self):
        cpu = CPU.Main(self.RAM, self.ROM, self.Opcode)
        cpu.Start_Executing_From_ROM()



def Main_Func():
    main = Main()

    main.LoadGB("tetris.gb")
    main.Execute()






if __name__ == "__main__":
    #Testing_Main()
    Main_Func()