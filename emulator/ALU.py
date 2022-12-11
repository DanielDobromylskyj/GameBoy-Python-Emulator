

class Core():
    def __init__(self, cpu, Binary):
        self.CPU = cpu
        self.Binary = Binary


    def ADD(self, Reg):
        for key in self.CPU.Registers.keys():
            if Reg in key:
                Reg = key
                break

        OutputValue = self.CPU.Registers[Reg].ReadDenary() + self.CPU.Registers["A"].ReadDenary()
        Carry = 0

        if OutputValue > 15:
            Carry = 1
            OutputValue = 15

        self.CPU.Registers["A"].WriteDenary(OutputValue)
        self.CPU.Registers["c"].WriteDenary(Carry) # Carry Should Really Only be 1 bit but oh well (its a 8bit reg not a 1 bit)

    def SUB(self, Reg):
        for key in self.CPU.Registers.keys():
            if Reg in key:
                Reg = key
                break

        OutputValue = self.CPU.Registers["A"].ReadDenary() - self.CPU.Registers[Reg].ReadDenary()
        Carry = 0

        if OutputValue > 15:
            Carry = 1
            OutputValue = 15

        self.CPU.Registers["A"].WriteDenary(OutputValue)
        self.CPU.Registers["c"].WriteDenary(Carry) # Carry Should Really Only be 1 bit but oh well (its a 8bit reg not a 1 bit)
