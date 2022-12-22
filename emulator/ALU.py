

class Core():
    def __init__(self, cpu, Binary):
        self.CPU = cpu
        self.Binary = Binary


    def ADD_8Bit(self, Big_Reg, Small_Reg=None):
        x = Big_Reg
        if Small_Reg != None: # This is done to allow a value to be passed OR A Register
            x = int(self.CPU.Registers[Big_Reg].ReadDenary(Small_Reg))
        try:
            OutputValue = x + int(self.CPU.Registers["AF"].ReadDenary("A"))
        except:
            print(x, type(x))
            print(self.CPU.Registers["AF"].ReadDenary("A"), type(self.CPU.Registers["AF"].ReadDenary("A")))
            OutputValue = 0

        Carry = 0

        if OutputValue > 15:
            Carry = 1
            OutputValue = 15

        self.CPU.Registers["AF"].WriteDenary(OutputValue, "A")
        self.CPU.Registers["c"].WriteDenary(Carry) # Carry Should Really Only be 1 bit but oh well (its a 8bit reg not a 1 bit)

    def SUB_8Bit(self, Big_Reg, Small_Reg=None):
        x = Big_Reg
        if Small_Reg != None: # This is done to allow a value to be passed OR A Register
            x = self.CPU.Registers[Big_Reg].ReadDenary(Small_Reg)

        OutputValue = self.CPU.Registers["AF"].ReadDenary("A") - x
        Carry = 0

        if OutputValue > 15:
            Carry = 1 # Unsure about this line here. It is SUB not ADD
            OutputValue = 15

        self.CPU.Registers["AF"].WriteDenary(OutputValue, "A")
        self.CPU.Registers["c"].WriteDenary(Carry) # Carry Should Really Only be 1 bit but oh well (its a 8bit reg not a 1 bit)

    def AND_8Bit(self, Big_Reg, Small_Reg=None):
        x = Big_Reg
        if Small_Reg != None: # This is done to allow a value to be passed OR A Register
            x = self.CPU.Registers[Big_Reg].ReadBinaryString(Small_Reg)
        x = list(x)
        y = list(self.CPU.Registers["AF"].ReadBinaryString("A"))

        OutputValue = ""
        for i in range(len(x)):
            if x[i] == y[i]:
                OutputValue = OutputValue + "1"
            else:
                OutputValue = OutputValue + "0"

        self.CPU.Registers["AF"].WriteBinaryString(OutputValue, "A")

    def OR_8Bit(self, Big_Reg, Small_Reg=None):
        x = Big_Reg
        if Small_Reg != None: # This is done to allow a value to be passed OR A Register
            x = self.CPU.Registers[Big_Reg].ReadBinaryString(Small_Reg)
        x = list(x)
        y = list(self.CPU.Registers["AF"].ReadBinaryString("A"))

        OutputValue = ""
        for i in range(len(x)):
            if (x[i] == "1") or (y[i] == "1"):
                OutputValue = OutputValue + "1"
            else:
                OutputValue = OutputValue + "0"

        self.CPU.Registers["AF"].WriteBinaryString(OutputValue, "A")

    def XOR_8Bit(self, Big_Reg, Small_Reg=None):
        x = Big_Reg
        if Small_Reg != None: # This is done to allow a value to be passed OR A Register
            x = self.CPU.Registers[Big_Reg].ReadBinaryString(Small_Reg)
        x = list(x)
        y = list(self.CPU.Registers["AF"].ReadBinaryString("A"))

        OutputValue = ""
        for i in range(len(x)):
            if (x[i] == "1") ^ (y[i] == "1"):
                OutputValue = OutputValue + "1"
            else:
                OutputValue = OutputValue + "0"

        self.CPU.Registers["AF"].WriteBinaryString(OutputValue, "A")

