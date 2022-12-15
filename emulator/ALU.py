

class Core():
    def __init__(self, cpu, Binary):
        self.CPU = cpu
        self.Binary = Binary


    def ADD_8Bit(self, Big_Reg, Small_Reg=None):
        x = Big_Reg
        if Small_Reg == None: # This is done to allow a value to be passed OR A Register
            x = self.CPU.Registers[Big_Reg].ReadDenary(Small_Reg)

        OutputValue = x + self.CPU.Registers["AF"].ReadDenary("A")
        Carry = 0

        if OutputValue > 15:
            Carry = 1
            OutputValue = 15

        self.CPU.Registers["AF"].WriteDenary(OutputValue, "A")
        self.CPU.Registers["c"].WriteDenary(Carry) # Carry Should Really Only be 1 bit but oh well (its a 8bit reg not a 1 bit)

    def SUB_8Bit(self, Big_Reg, Small_Reg=None):
        x = Big_Reg
        if Small_Reg == None: # This is done to allow a value to be passed OR A Register
            x = self.CPU.Registers[Big_Reg].ReadDenary(Small_Reg)

        OutputValue = self.CPU.Registers["AF"].ReadDenary("A") - x
        Carry = 0

        if OutputValue > 15:
            Carry = 1 # Unsure about this line here. It is SUB not ADD
            OutputValue = 15

        self.CPU.Registers["AF"].WriteDenary(OutputValue, "A")
        self.CPU.Registers["c"].WriteDenary(Carry) # Carry Should Really Only be 1 bit but oh well (its a 8bit reg not a 1 bit)
