

class Core():
    def __init__(self, cpu, Binary):
        self.CPU = cpu
        self.Binary = Binary

        # Flags - https://www.codeproject.com/Articles/1108304/Z-CPU-Flag-Register
        self.FlagTable = {"Z":3, "N":2, "H":1, "C":0} # I am not sure what they actually are. I dont see the flag value used anywhere. Should be fine
        self.Flags = "0000000"

    def SetFlag(self, Flag, Reset=False):
        # Get Pos In Byte
        Pos = 7 - self.FlagTable[Flag]
        #Get Value
        X = "1"
        if Reset: X = "0"
        # Set Bit
        self.Flags = self.Flags[:Pos] + X + self.Flags[Pos:]
    def ReadFlag(self, Flag):
        return self.Flags[self.FlagTable[Flag]]



    def ADD_8Bit(self, Big_Reg, Small_Reg=None, Cary=False):
        x = Big_Reg
        if Small_Reg != None: # This is done to allow a value to be passed OR A Register
            x = int(self.CPU.Registers[Big_Reg].ReadDenary(Small_Reg))
        try:
            OutputValue = x + int(self.CPU.Registers["AF"].ReadDenary("A"))
            if Cary == True:
                OutputValue += int(self.ReadFlag("C"))
        except:
            OutputValue = 0


        Carry = False

        if OutputValue > 255:
            Carry = True

        self.CPU.Registers["AF"].WriteDenary(OutputValue, "A")
        self.SetFlag("C", Carry)

    def SUB_8Bit(self, Big_Reg, Small_Reg=None, Cary=False):
        x = Big_Reg
        if Small_Reg != None: # This is done to allow a value to be passed OR A Register
            x = self.CPU.Registers[Big_Reg].ReadDenary(Small_Reg)

        OutputValue = self.CPU.Registers["AF"].ReadDenary("A") - x
        if Cary == True:
            OutputValue -= int(self.ReadFlag("C"))

        Carry = False
        if OutputValue < 0:
            Carry = True


        self.CPU.Registers["AF"].WriteDenary(OutputValue, "A")
        self.SetFlag("C", Carry)

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

