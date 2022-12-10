# Binary Module, Used To Store Data in Registers and
# Form an interface between the CPU Values & The ALU


def Invert_8bit(x):
    return 8 - x
def Invert_16bit(x):
    return 16 - x

class _8bit():
    def __init__(self):
        self.Value = ["0","0","0","0","0","0","0","0"]


    def WriteDenary(self, Value):
        self.Value = ["0", "0", "0", "0", "0", "0", "0", "0"] # Reset Value
        Power = 7
        while (Value > 0) and (Power > 0):
            if 2 ** Power <= Value:
                self.Value[Invert_8bit(2 ** Power)] = '1'
            Power -= 1

    def ReadDenary(self):
        Power = 7
        Output = 0
        for diget in self.Value:
            Output += (int(diget) * 2) ** Power
            Power -= 1

        return Output - 1

    def WriteBinaryString(self, Value):
        self.Value = list(Value)

    def ReadBinaryString(self):
        return "".join(self.Value)

class _16bit():
    def __init__(self, Reg_A_Name,  _8bit_reg_a, Reg_B_Name, _8bit_reg_b):
        self.RegA = _8bit_reg_a
        self.NameA = Reg_A_Name
        self.RegB = _8bit_reg_b
        self.NameB = Reg_B_Name


    def WriteDenary(self, Value, Register="16bit"):
        if len(Register) == 1:
            if Register == self.NameA:
                self.RegA.WriteDenary(Value)
            else:
                self.RegB.WriteDenary(Value)
        else:
            A = Value
            if Value > 15: A = 15

            self.RegA.WriteDenary(A)
            self.RegB.WriteDenary(Value // 16)



    def ReadDenary(self, Register="16bit"):
        if len(Register) == 1:
            if Register == self.NameA:
                return self.RegA.ReadDenary()
            return self.RegB.ReadDenary()
        else:
            x = self.RegB.ReadDenary()
            return self.RegA.ReadDenary() + x


    def WriteBinaryString(self, Value, Register="16bit"):
        if len(Register) == 1:
            if Register == self.NameA:
                x = self.RegA
            else:
                x = self.RegB

            x.Value = list(Value)

        else:
            self.RegA.Value = list(Value[0:8])
            self.RegB.Value = list(Value[8:16])



    def ReadBinaryString(self, Register="16bit"): # Not Working
        if len(Register) >= 2:
            return "".join(self.RegA.Value) + "".join(self.RegB.Value)
        if Register == self.NameA:
            return "".join(self.RegA.Value)
        return "".join(self.RegB.Value)



def LeftShift(x): # Normal Binary Shift - 1 Position
    Data = x.ReadBinaryString() # e.g. 0010010
    x.WriteBinaryString(Data[1:] + "0")

def RightShift(x):
    Data = x.ReadBinaryString() # e.g. 0010010
    x.WriteBinaryString("0" + Data[:-1])

def LeftCycle(x): # Binary Shift But We Loop The Bit thats removed to where the "new" bit is
    Data = x.ReadBinaryString() # e.g. 0010010
    x.WriteBinaryString(Data[1:] + Data[0])

def RightCycle(x):
    Data = x.ReadBinaryString() # e.g. 0010010
    x.WriteBinaryString(Data[-0] + Data[:-1])



if __name__ == "__main__":

    _16BitReg = _16bit("A", _8bit(), "B", _8bit())

    _16BitReg.WriteBinaryString("1001000000001111", "AB")
    print(_16BitReg.ReadBinaryString("AB"))

    LeftShift(_16BitReg)

    print(_16BitReg.ReadBinaryString("AB"))
    print(_16BitReg.ReadBinaryString("A"))
    print(_16BitReg.ReadBinaryString("B"))