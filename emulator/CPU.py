import time




class Main():
    def __init__(self, RAM, ROM, Opcodes, CMNDS, BIN, ALU):
        self.ROM, self.RAM, self.Opcodes, self.CM, self.binary, self.alu = ROM, RAM.RAM(), Opcodes, CMNDS, BIN, ALU


        self.NextLineNumber = 0
        self.Halted = False
        self.WaitingInterupt = False
        self.Interupt = False

        # Settings
        self.SkipWaits = False # Skip STOP / HALT Commands?

        # Create Registers
        alpha = "BC,DE,HL,SP,AF,c".split(",") # c = Carry (CY)
        self.Registers = {}
        for letter in alpha:
            if len(letter) == 1:
                self.Registers[letter] = self.binary._8bit() #RAM.Register(letter)
            else:
                x = self.binary._16bit(letter[0], self.binary._8bit(), letter[1], self.binary._8bit()) # Creates 2 8bit registers then combines Them
                x.WriteBinaryString("0000000000000000")
                self.Registers[letter] = x

        # Testing Code

        # ------------
        self.ALU = self.alu.Core(self, self.binary) # Init the ALU

    def Start_Executing_From_ROM(self):
        LineNumber = 0

        self.Go = 0
        for i in range(self.ROM.FileSize):
            if LineNumber >= self.ROM.FileSize + self.Go:
                break

            if self.WaitingInterupt:
                self.Wait()

            HEX = self.ROM.Read(LineNumber) # Read Hex Value

            if "NextLineNumber" not in self.Opcodes.ToPython(HEX):
                self.NextLineNumber += 1

            self.ExecuteHEX(HEX) # Execute The HEX



            LineNumber = int(str(self.NextLineNumber)) # Change The Line Number

        print("[Emulator][CPU] Finished Executing Program")
        self.Dump()

    def Dump(self):
        print("[Emulator][DUMP] Dumping Registers To dump/registers.dump")
        x = ""
        for key in self.Registers.keys():
            x = x + "\nRegister (Denary): " + str(key) + " Data: " +  str(self.Registers[key].ReadDenary())
            x = x + "\nRegister (Binary): " + str(key) + " Data: " +  str(self.Registers[key].ReadBinaryString())
        # registers.dump
        print("[Emulator][DUMP] Dumping RAM To dump/ram.dump")
        f = open("dump/ram.dump", "w")
        f.write(str(self.RAM.Data))
        f.close()
        f = open("dump/registers.dump", "w")
        f.write(x)
        f.close()

        return x


    def ExecuteHEX(self, HEX):
        # Allows for cleaner writing of codes / HEX to Python
        Register = self.Registers
        Prefix = self.Opcodes.PrefixTable
        binary = self.binary
        ALU = self.ALU
        memory = self.RAM
        instructions = self.ROM
        system = self

        t = self.Opcodes.ToPython(HEX)
        try:
            exec(t)
        except Exception as e:
            print("[Emulator][Core] Failed To Execute Command:", e)
            print("[Emulator][Core] Line Error:", t, HEX)

    def Wait(self): # Await For Interupt
        if self.SkipWaits != True:
            print("Awaiting Interupr")
            while True:
                time.sleep(0.05)
                if self.Interupt:
                    self.Interupt = False
                    self.WaitingInterupt = False
                    return

    def Halt(self):
        self.Halted = True

    def Stop(self): # Hmmm - WAIT FOR EXTERNAL INPUT? What is that?
        self.NextLineNumber += 1
        self.WaitingInterupt = True


    def Decode(self, hex):
        if type(hex) != int:
            return int("0x" + str(hex), 0)
        return hex