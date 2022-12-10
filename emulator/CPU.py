




class Main():
    def __init__(self, RAM, ROM, Opcodes, CMNDS, BIN, ALU):
        self.ROM, self.RAM, self.Opcodes, self.CM, self.binary, self.alu = ROM, RAM.RAM(), Opcodes, CMNDS, BIN, ALU


        self.NextLineNumber = 1

        # Create Registers
        alpha = "BC,DE,HL,SP,A,c".split(",") # c = Carry (CY)
        self.Registers = {}
        for letter in alpha:
            if len(letter) == 1:
                self.Registers[letter] = self.binary._8bit() #RAM.Register(letter)
            else:
                x = self.binary._16bit(letter[0], self.binary._8bit(), letter[1], self.binary._8bit()) # Creates 2 8bit registers
                x.WriteBinaryString("0000000000000000")
                self.Registers[letter] = x
                                                                                                                            # then combines Them

        self.ALU = self.alu.Core(self, self.binary) # Init the ALU

        self.ALU.ADD("B")

    def Start_Executing_From_ROM(self):
        LineNumber = 0
        for i in range(self.ROM.FileSize):
            self.NextLineNumber += 1 # We do it now so it doesn't interupt the jump command blah blah blah

            HEX = self.ROM.Read(LineNumber) # Read Hex Value
            self.ExecuteHEX(HEX) # Execute The HEX

            LineNumber = int(str(self.NextLineNumber)) # Change The Line Number





    def ExecuteHEX(self, HEX):
        # Allows for cleaner writing of codes / HEX to Python
        CMD = self.CM # Lets u sdo things like shifting binary and other stuff like that
        Register = self.Registers
        Prefix = self.Opcodes.PrefixTable
        binary = self.binary

        exec(self.Opcodes.ToPython(HEX))


