import math
# Binary Module, Used To Store Data in Registers and
# Form an interface between the CPU Values & The ALU



def FromDecimal(n): # 8 bit only
    binary = bin(n).replace("0b", "")
    return "0" * (8 - len(binary)) + binary


def Invert_8bit(x):
    return 7 - x
def Invert_16bit(x):
    return 16 - x

class _8bit():
    def __init__(self):
        self.Value = ["0","0","0","0","0","0","0","0"]


    def WriteDenary(self, Value): # Not Working
        self.Value = ["0", "0", "0", "0", "0", "0", "0", "0"] # Reset Value
        Power = 8
        if Value < 0: Value *= -1 # Make it always Positive

        while (Value > 0) and (Power > -1):
            if 2 ** Power <= Value:
                self.Value[Invert_8bit(Power)] = '1'
                Value -= (2**Power)
            Power -= 1



    def ReadDenary(self):
        Power = 8
        Output = 0
        for diget in self.Value:
            if diget == "1":
                Output +=  2 ** Power
            Power -= 1

        return Output // 2

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
        Value = int(Value)
        if len(Register) == 1:
            if Register == self.NameA:
                self.RegA.WriteDenary(Value)
            elif Register == self.NameB:
                self.RegB.WriteDenary(Value)
            else: print("[Emulator][Binary] WD :", Register, "Is Not In This 'Double'")
        else:# 16bit reg : 8BitReg(B) , 8BitReg(A)
            ByteB = math.floor(Value / 256) # 256 == 8bits / Removes Register A's Byte, Just leaving Byte B
            ByteA = Value - (ByteB * 256)  # Byte A == Value - Whats In Register B

            self.RegA.WriteDenary(ByteA)
            self.RegB.WriteDenary(ByteB)

    def WriteBinaryString(self, Value, Register="16bit"):
        if len(Register) == 1:
            if Register == self.NameA:
                self.RegA.WriteBinaryString(Value)
            elif Register == self.NameB:
                self.RegB.WriteBinaryString(Value)
            else: print("[Emulator][Binary] WB :", Register, "Is Not In This 'Double'")
        else:
            self.RegA.WriteBinaryString(Value[8:16])
            self.RegB.WriteBinaryString(Value[0:8])


    def ReadDenary(self, Register="16bit"):
        if len(Register) == 1:
            if Register == self.NameA:
                return self.RegA.ReadDenary()
            elif Register == self.NameB:
                return self.RegB.ReadDenary()
            else:
                print("[Emulator][Binary] RD :", Register, "Is Not In This 'Double'")
        else:
            ByteA = self.RegA.ReadDenary() # This Doesn't Need To Be Modified
            ByteB = self.RegB.ReadDenary() * 256# Shift it back to its 'Original' Position
            return ByteB + ByteA

    def ReadBinaryString(self, Register="16bit"):
        if len(Register) == 1:
            if Register == self.NameA:
                return self.RegA.ReadBinaryString()
            elif Register == self.NameB:
                return self.RegB.ReadBinaryString()
            else:
                print("[Emulator][Binary] RB :", Register, "Is Not In This 'Double'")
        else:
            return self.RegB.ReadBinaryString() + self.RegA.ReadBinaryString()


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
def Increment(x, y=None):
    if y == None:
        Data = x.ReadDenary()
        x.WriteDenary(int(Data) + 1)
    else:
        Data = x.ReadDenary(y)
        x.WriteDenary(int(Data) + 1, y)
def Decrement(x, y=None):
    if y == None:
        Data = x.ReadDenary()
        x.WriteDenary(int(Data) - 1)
    else:
        Data = x.ReadDenary(y)
        x.WriteDenary(int(Data) - 1, y)



if __name__ == "__main__":
    # Demo
    print("Running 8 Bit Tests")
    _8BitReg = _8bit()

    _8BitReg.WriteDenary(13)
    if _8BitReg.ReadBinaryString() != "00001101":
        print("Test 1 Failed", _8BitReg.ReadBinaryString())
    if _8BitReg.ReadDenary() != 13:
        print("Test 2 Failed",  _8BitReg.ReadDenary())

    _8BitReg.WriteBinaryString("00001001")
    if _8BitReg.ReadBinaryString() != "00001001":
        print("Test 3 Failed", _8BitReg.ReadBinaryString())
    if _8BitReg.ReadDenary() != 9:
        print("Test 4 Failed", _8BitReg.ReadDenary())

if __name__ == "__main__":
    # 16 BIT TESTING SCRIPT STARTS HERE
    print("Running 16 Bit Tests")
    _16BitReg = _16bit("A", _8bit(), "B", _8bit())

    _16BitReg.WriteDenary(527)
    if _16BitReg.ReadBinaryString() != "0000001000001111":
        print("Test 1 Failed", _16BitReg.ReadBinaryString())
    if _16BitReg.ReadDenary() != 527:
        print("Test 2 Failed", _16BitReg.ReadDenary())

    _16BitReg.WriteBinaryString("0000001000001111")

    if _16BitReg.ReadBinaryString() != "0000001000001111":
        print("Test 3 Failed", _16BitReg.ReadBinaryString())
    if _16BitReg.ReadDenary() != 527:
        print("Test 4 Failed", _16BitReg.ReadDenary())



