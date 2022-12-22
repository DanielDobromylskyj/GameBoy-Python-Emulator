

class Codes():
    def __init__(self):
        self.CodesToPython = {
            "00": [""],  # NOP (No-Op / No Oporation)                                                                   DONE
            "01": ["x = instructions.Read(system.NextLineNumber)",
                   "y = instructions.Read(system.NextLineNumber + 1)",     #                                            POSSIBLE PROBLEM >> x + y or y + x?
                   "Register['BC'].WriteDenary(system.Decode(x + y))",
                   "system.NextLineNumber += 3"],  # LD BC d16                                                          UNSURE
            "02": ["memory.Write(Register['BC'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))"],  #         NOTEST
            "03": ["binary.Increment(Register['BC'])"],  #                                                              NOTEST
            "04": ["binary.Increment(Register['BC'], 'B')"],  #                                                         NOTEST
            "05": ["binary.Decrement(Register['BC'], 'B')"],  #                                                         NOTEST
            "06": ["Register['BC'].WriteDenary(system.Decode(instructions.Read(system.NextLineNumber)), 'B')",
                   "system.NextLineNumber += 2"],     #                                                         NOTEST
            "07": [""],
            "08": [""],
            "09": [""],
            "0a": [""],
            "0b": [""],
            "0c": [""],
            "0d": [""],
            "0e": [""],
            "0f": [""],

            "10": ["system.Stop()"], # Stop CPU                                                                         UNSURE/UNKNOWN
            "11": ["x = instructions.Read(system.NextLineNumber)",
                   "y = instructions.Read(system.NextLineNumber + 1)",     #                                            POSSIBLE PROBLEM >> x + y or y + x?
                   "Register['DE'].WriteDenary(system.Decode(x + y))",
                   "system.NextLineNumber += 3"],  # LD BC d16                                                       UNSURE
            "12": ["memory.Write(Register['DE'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))"],  #         NOTEST
            "13": ["binary.Increment(Register['DE'])"],  #                                                              NOTEST
            "14": ["binary.Increment(Register['DE'], 'D')"],  #                                                         NOTEST
            "15": ["binary.Decrement(Register['DE'], 'D')"],  #                                                         NOTEST
            "16": ["Register['DE'].WriteDenary(system.Decode(instructions.Read(system.NextLineNumber)), 'D')",
                   "system.NextLineNumber += 2"],     #                                                         NOTEST
            "17": [""],
            "18": [""],
            "19": [""],
            "1a": [""],
            "1b": [""],
            "1c": [""],
            "1d": [""],
            "1e": [""],
            "1f": [""],

            "20": [""], #                                                                                               UNKNOWN
            "21": ["x = instructions.Read(system.NextLineNumber)",
                   "y = instructions.Read(system.NextLineNumber + 1)",     #                                            POSSIBLE PROBLEM >> x + y or y + x?
                   "Register['HL'].WriteDenary(system.Decode(x + y))",
                   "system.NextLineNumber += 3"],  #                                                                 UNSURE
            "22": ["binary.Increment(Register['AF'], 'A')",
                   "memory.Write(Register['HL'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))",
                   "binary.Decrement(Register['AF'], 'A')"],  #                                                         NOTEST
            "23": ["binary.Increment(Register['HL'])"],  #                                                              NOTEST
            "24": ["binary.Increment(Register['HL'], 'H')"],  #                                                         NOTEST
            "25": ["binary.Decrement(Register['HL'], 'H')"],  #                                                         NOTEST
            "26": ["Register['HL'].WriteDenary(system.Decode(instructions.Read(system.NextLineNumber)), 'H')",
                   "system.NextLineNumber += 2"],  #                                                            NOTEST
            "27": [""],
            "28": [""],
            "29": [""],
            "2a": [""],
            "2b": [""],
            "2c": [""],
            "2d": [""],
            "2e": [""],
            "2f": [""],

            "30": [""],  # UNKNOWN
            "31": ["x = instructions.Read(system.NextLineNumber)",
                   "y = instructions.Read(system.NextLineNumber + 1)",     #                                            POSSIBLE PROBLEM >> x + y or y + x?
                   "Register['SP'].WriteDenary(system.Decode(x + y))",
                   "system.NextLineNumber += 3"],  #                                                                    NOTEST
            "32": ["binary.Decrement(Register['AF'], 'A')",
                   "memory.Write(Register['HL'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))",
                   "binary.Increment(Register['AF'], 'A')"],  #                                                         NOTEST
            "33": ["binary.Increment(Register['SP'])"],  #                                                              NOTEST
            "34": ["binary.Increment(Register['HL'], 'H')"],  #                                                         NOTEST
            "35": ["binary.Decrement(Register['SP'])"],  #                                                              NOTEST
            "36": ["Register['HL'].WriteDenary(system.Decode(instructions.Read(system.NextLineNumber)))",
                   "system.NextLineNumber += 2"],  #                                                            NOTEST
            "37": [""],
            "38": [""],
            "39": [""],
            "3a": [""],
            "3b": [""],
            "3c": [""],
            "3d": [""],
            "3e": [""],
            "3f": [""],

            "40": ["Register['BC'].WriteBinaryString(Register['BC'].ReadBinaryString('B'),'B')"],
            "41": ["Register['BC'].WriteBinaryString(Register['BC'].ReadBinaryString('C'),'B')"],
            "42": ["Register['BC'].WriteBinaryString(Register['DE'].ReadBinaryString('D'),'B')"],
            "43": ["Register['BC'].WriteBinaryString(Register['DE'].ReadBinaryString('E'),'B')"],
            "44": ["Register['BC'].WriteBinaryString(Register['HL'].ReadBinaryString('H'),'B')"],
            "45": ["Register['BC'].WriteBinaryString(Register['HL'].ReadBinaryString('L'),'B')"],
            "46": ["Register['BC'].WriteBinaryString(memory.Read(Register['HL'].ReadBinaryString()),'B')"],
            "47": ["Register['BC'].WriteBinaryString(Register['AF'].ReadBinaryString('A'),'B')"],
            "48": ["Register['BC'].WriteBinaryString(Register['BC'].ReadBinaryString('B'),'C')"],
            "49": ["Register['BC'].WriteBinaryString(Register['BC'].ReadBinaryString('C'),'C')"],
            "4a": ["Register['BC'].WriteBinaryString(Register['DE'].ReadBinaryString('D'),'C')"],
            "4b": ["Register['BC'].WriteBinaryString(Register['DE'].ReadBinaryString('E'),'C')"],
            "4c": ["Register['BC'].WriteBinaryString(Register['HL'].ReadBinaryString('H'),'C')"],
            "4d": ["Register['BC'].WriteBinaryString(Register['HL'].ReadBinaryString('L'),'C')"],
            "4e": ["Register['BC'].WriteBinaryString(memory.Read(Register['HL'].ReadBinaryString()),'C')"],
            "4f": ["Register['BC'].WriteBinaryString(Register['AF'].ReadBinaryString('A'),'C')"],

            "50": ["Register['DE'].WriteBinaryString(Register['BC'].ReadBinaryString('B'),'D')"],
            "51": ["Register['DE'].WriteBinaryString(Register['BC'].ReadBinaryString('C'),'D')"],
            "52": ["Register['DE'].WriteBinaryString(Register['DE'].ReadBinaryString('D'),'D')"],
            "53": ["Register['DE'].WriteBinaryString(Register['DE'].ReadBinaryString('E'),'D')"],
            "54": ["Register['DE'].WriteBinaryString(Register['HL'].ReadBinaryString('H'),'D')"],
            "55": ["Register['DE'].WriteBinaryString(Register['HL'].ReadBinaryString('L'),'D')"],
            "56": ["Register['DE'].WriteBinaryString(memory.Read(Register['HL'].ReadBinaryString()),'D')"],
            "57": ["Register['DE'].WriteBinaryString(Register['AF'].ReadBinaryString('A'),'D')"],
            "58": ["Register['DE'].WriteBinaryString(Register['BC'].ReadBinaryString('B'),'E')"],
            "59": ["Register['DE'].WriteBinaryString(Register['BC'].ReadBinaryString('C'),'E')"],
            "5a": ["Register['DE'].WriteBinaryString(Register['DE'].ReadBinaryString('D'),'E')"],
            "5b": ["Register['DE'].WriteBinaryString(Register['DE'].ReadBinaryString('E'),'E')"],
            "5c": ["Register['DE'].WriteBinaryString(Register['HL'].ReadBinaryString('H'),'E')"],
            "5d": ["Register['DE'].WriteBinaryString(Register['HL'].ReadBinaryString('L'),'E')"],
            "5e": ["Register['DE'].WriteBinaryString(memory.Read(Register['HL'].ReadBinaryString()),'E')"],
            "5f": ["Register['DE'].WriteBinaryString(Register['AF'].ReadBinaryString('A'),'E')"],

            "60": ["Register['HL'].WriteBinaryString(Register['BC'].ReadBinaryString('B'),'H')"],
            "61": ["Register['HL'].WriteBinaryString(Register['BC'].ReadBinaryString('C'),'H')"],
            "62": ["Register['HL'].WriteBinaryString(Register['DE'].ReadBinaryString('D'),'H')"],
            "63": ["Register['HL'].WriteBinaryString(Register['DE'].ReadBinaryString('E'),'H')"],
            "64": ["Register['HL'].WriteBinaryString(Register['HL'].ReadBinaryString('H'),'H')"],
            "65": ["Register['HL'].WriteBinaryString(Register['HL'].ReadBinaryString('L'),'H')"],
            "66": ["Register['HL'].WriteBinaryString(memory.Read(Register['HL'].ReadBinaryString()),'H')"],
            "67": ["Register['HL'].WriteBinaryString(Register['AF'].ReadBinaryString('A'),'H')"],
            "68": ["Register['HL'].WriteBinaryString(Register['BC'].ReadBinaryString('B'),'L')"],
            "69": ["Register['HL'].WriteBinaryString(Register['BC'].ReadBinaryString('C'),'L')"],
            "6a": ["Register['HL'].WriteBinaryString(Register['DE'].ReadBinaryString('D'),'L')"],
            "6b": ["Register['HL'].WriteBinaryString(Register['DE'].ReadBinaryString('E'),'L')"],
            "6c": ["Register['HL'].WriteBinaryString(Register['HL'].ReadBinaryString('H'),'L')"],
            "6d": ["Register['HL'].WriteBinaryString(Register['HL'].ReadBinaryString('L'),'L')"],
            "6e": ["Register['HL'].WriteBinaryString(memory.Read(Register['HL'].ReadBinaryString()),'L')"],
            "6f": ["Register['HL'].WriteBinaryString(Register['AF'].ReadBinaryString('A'),'L')"],

            "70": ["memory.Write(Register['HL'].ReadBinaryString(), Register['BC'].ReadBinaryString('B'))"],
            "71": ["memory.Write(Register['HL'].ReadBinaryString(), Register['BC'].ReadBinaryString('C'))"],
            "72": ["memory.Write(Register['HL'].ReadBinaryString(), Register['DE'].ReadBinaryString('D'))"],
            "73": ["memory.Write(Register['HL'].ReadBinaryString(), Register['DE'].ReadBinaryString('E'))"],
            "74": ["memory.Write(Register['HL'].ReadBinaryString(), Register['HL'].ReadBinaryString('H'))"],
            "75": ["memory.Write(Register['HL'].ReadBinaryString(), Register['HL'].ReadBinaryString('L'))"],
            "76": ["system.Halt()"],
            "77": ["memory.Write(Register['HL'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))"],
            "78": ["Register['AF'].WriteBinaryString(Register['BC'].ReadBinaryString('B'),'A')"],
            "79": ["Register['AF'].WriteBinaryString(Register['BC'].ReadBinaryString('C'),'A')"],
            "7a": ["Register['AF'].WriteBinaryString(Register['DE'].ReadBinaryString('D'),'A')"],
            "7b": ["Register['AF'].WriteBinaryString(Register['DE'].ReadBinaryString('E'),'A')"],
            "7c": ["Register['AF'].WriteBinaryString(Register['HL'].ReadBinaryString('H'),'A')"],
            "7d": ["Register['AF'].WriteBinaryString(Register['HL'].ReadBinaryString('L'),'A')"],
            "7e": ["Register['AF'].WriteBinaryString(memory.Read(Register['HL'].ReadBinaryString()),'A')"],
            "7f": ["Register['AF'].WriteBinaryString(Register['AF'].ReadBinaryString('A'),'A')"],

            "80": ["ALU.ADD_8Bit('BC', 'B')"],
            "81": ["ALU.ADD_8Bit('BC', 'C')"],
            "82": ["ALU.ADD_8Bit('DE', 'D')"],
            "83": ["ALU.ADD_8Bit('DE', 'E')"],
            "84": ["ALU.ADD_8Bit('HL', 'H')"],
            "85": ["ALU.ADD_8Bit('HL', 'L')"],
            "86": ["ALU.ADD_8Bit(memory.Read(Register['BC'].ReadBinaryString()))"],
            "87": ["ALU.ADD_8Bit('AF', 'B')"],
            "88": [""],
            "89": [""],
            "8a": [""],
            "8b": [""],
            "8c": [""],
            "8d": [""],
            "8e": [""],
            "8f": [""],

            "90": ["ALU.SUB_8Bit('BC', 'B')"],
            "91": ["ALU.SUB_8Bit('BC', 'C')"],
            "92": ["ALU.SUB_8Bit('DE', 'D')"],
            "93": ["ALU.SUB_8Bit('DE', 'E')"],
            "94": ["ALU.SUB_8Bit('HL', 'H')"],
            "95": ["ALU.SUB_8Bit('HL', 'L')"],
            "96": ["ALU.SUB_8Bit(memory.Read(Register['BC'].ReadBinaryString()))"],
            "97": ["ALU.SUB_8Bit('AF', 'B')"],
            "98": [""],
            "99": [""],
            "9a": [""],
            "9b": [""],
            "9c": [""],
            "9d": [""],
            "9e": [""],
            "9f": [""],

            "a0": ["ALU.AND_8Bit('BC', 'B')"],
            "a1": ["ALU.AND_8Bit('BC', 'C')"],
            "a2": ["ALU.AND_8Bit('DE', 'D')"],
            "a3": ["ALU.AND_8Bit('DE', 'E')"],
            "a4": ["ALU.AND_8Bit('HL', 'H')"],
            "a5": ["ALU.AND_8Bit('HL', 'L')"],
            "a6": ["ALU.AND_8Bit(memory.Read(Register['BC'].ReadBinaryString()))"],
            "a7": ["ALU.AND_8Bit('AF', 'A')"],
            "a8": ["ALU.XOR_8Bit('BC', 'B')"],
            "a9": ["ALU.XOR_8Bit('BC', 'C')"],
            "aa": ["ALU.XOR_8Bit('DE', 'D')"],
            "ab": ["ALU.XOR_8Bit('DE', 'E')"],
            "ac": ["ALU.XOR_8Bit('HL', 'H')"],
            "ad": ["ALU.XOR_8Bit('HL', 'L')"],
            "ae": ["ALU.XOR_8Bit(memory.Read(Register['BC'].ReadBinaryString()))"],
            "af": ["ALU.XOR_8Bit('AF', 'A')"],

            "b0": ["ALU.OR_8Bit('BC', 'B')"],
            "b1": ["ALU.OR_8Bit('BC', 'C')"],
            "b2": ["ALU.OR_8Bit('DE', 'D')"],
            "b3": ["ALU.OR_8Bit('DE', 'E')"],
            "b4": ["ALU.OR_8Bit('HL', 'H')"],
            "b5": ["ALU.OR_8Bit('HL', 'L')"],
            "b6": ["ALU.OR_8Bit(memory.Read(Register['BC'].ReadBinaryString()))"],
            "b7": ["ALU.OR_8Bit('AF', 'A')"],
            "b8": [""],
            "b9": [""],
            "ba": [""],
            "bb": [""],
            "bc": [""],
            "bd": [""],
            "be": [""],
            "bf": [""],

            "c0": [""],
            "c1": [""],
            "c2": [""],
            "c3": [""],
            "c4": [""],
            "c5": [""],
            "c6": ["ALU.ADD_8Bit(system.Decode(instructions.Read(system.NextLineNumber)))",
                   "system.NextLineNumber += 2"],
            "c7": [""],
            "c8": [""],
            "c9": [""],
            "ca": [""],
            "cb": [""],
            "cc": [""],
            "cd": [""],
            "ce": [""],
            "cf": [""],

            "d0": [""],
            "d1": [""],
            "d2": [""],
            "d3": [""],
            "d4": [""],
            "d5": [""],
            "d6": ["ALU.SUB_8Bit(system.Decode(instructions.Read(system.NextLineNumber)))",
                   "system.NextLineNumber += 2"],
            "d7": [""],
            "d8": [""],
            "d9": [""],
            "da": [""],
            "db": [""],
            "dc": [""],
            "dd": [""],
            "de": [""],
            "df": [""],

            "e0": [""],
            "e1": [""],
            "e2": [""],
            "e3": [""],
            "e4": [""],
            "e5": [""],
            "e6": ["ALU.AND_8Bit(binary.FromDecimal(system.Decode(instructions.Read(system.NextLineNumber))))",
                   "system.NextLineNumber += 2"],
            "e7": [""],
            "e8": [""],
            "e9": [""],
            "ea": [""],
            "eb": [""],
            "ec": [""],
            "ed": [""],
            "ee": ["ALU.XOR_8Bit(binary.FromDecimal(system.Decode(instructions.Read(system.NextLineNumber))))",
                   "system.NextLineNumber += 2"],
            "ef": [""],

            "f0": [""],
            "f1": [""],
            "f2": [""],
            "f3": [""],
            "f4": [""],
            "f5": [""],
            "f6": ["ALU.OR_8Bit(binary.FromDecimal(system.Decode(instructions.Read(system.NextLineNumber))))",
                   "system.NextLineNumber += 2"],
            "f7": [""],
            "f8": [""],
            "f9": [""],
            "fa": [""],
            "fb": [""],
            "fc": [""],
            "fd": [""],
            "fe": [""],
            "ff": [""],



        }

        self.PrefixTable = {
            # RLC - This Chunk Is Incorrect - Doesn't use the carry REG
            "00": ["binary.LeftShift(Register['B'])"],
            "01": ["binary.LeftShift(Register['C'])"],
            "02": ["binary.LeftShift(Register['D'])"],
            "03": ["binary.LeftShift(Register['E'])"],
            "04": ["binary.LeftShift(Register['H'])"],
            "05": ["binary.LeftShift(Register['L'])"],
            "06": ["binary.LeftShift(Register['HL'])"],
            "07": ["binary.LeftShift(Register['A'])"],
            # RRC - This Chunk Is Incorrect - Doesn't use the carry REG
            "08": ["binary.RightShift(Register['B'])"],
            "09": ["binary.RightShift(Register['C'])"],
            "0a": ["binary.RightShift(Register['D'])"],
            "0b": ["binary.RightShift(Register['E'])"],
            "0c": ["binary.RightShift(Register['H'])"],
            "0d": ["binary.RightShift(Register['L'])"],
            "0e": ["binary.RightShift(Register['HL'])"],
            "0f": ["binary.RightShift(Register['A'])"],

            # RL
            "10": ["binary.LeftShift(Register['B'])"],
            "11": ["binary.LeftShift(Register['C'])"],
            "12": ["binary.LeftShift(Register['D'])"],
            "13": ["binary.LeftShift(Register['E'])"],
            "14": ["binary.LeftShift(Register['H'])"],
            "15": ["binary.LeftShift(Register['L'])"],
            "16": ["binary.LeftShift(Register['HL'])"],
            "17": ["binary.LeftShift(Register['A'])"],
            # RR
            "18": ["binary.RightShift(Register['B'])"],
            "19": ["binary.RightShift(Register['C'])"],
            "1a": ["binary.RightShift(Register['D'])"],
            "1b": ["binary.RightShift(Register['E'])"],
            "1c": ["binary.RightShift(Register['H'])"],
            "1d": ["binary.RightShift(Register['L'])"],
            "1e": ["binary.RightShift(Register['HL'])"],
            "1f": ["binary.RightShift(Register['A'])"],

        }





    def ToPython(self, code):
        try:
            return "\n".join(self.CodesToPython[code])
        except KeyError:
            print("[Emulator][Decoder] Opcode not found for:", code)
            return ""