




class Main():
    def __init__(self, RAM, ROM, Opcodes):
        self.ROM, self.RAM, self.Opcodes = ROM, RAM, Opcodes

        self.NextLineNumber = 1


    def Start_Executing_From_ROM(self):
        LineNumber = 0
        for i in range(self.ROM.FileSize):
            self.NextLineNumber += 1 # We do it now so it doesn't interupt the jump command blah blah blah

            HEX = self.ROM.Read(LineNumber) # Read Hex Value
            self.ExecuteHEX(HEX) # Execute The HEX

            LineNumber = int(str(self.NextLineNumber)) # Change The Line Number





    def ExecuteHEX(self, HEX):
        exec(self.Opcodes.ToPython(HEX))


