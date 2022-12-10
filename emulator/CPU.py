




class Main():
    def __init__(self, RAM, ROM, Opcodes, CMNDS):
        self.ROM, self.RAM, self.Opcodes, self.CM = ROM, RAM.RAM(), Opcodes, CMNDS


        self.NextLineNumber = 1

        # Create Registers
        alpha = list("ABCDEHL")
        self.Registers = {}
        for letter in alpha:
            self.Registers[letter] = RAM.Register()


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

        exec(self.Opcodes.ToPython(HEX))


