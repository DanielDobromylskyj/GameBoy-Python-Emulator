

class Codes():
    def __init__(self):
        self.CodesToPython = {
            "00": [""],  # NOP (No-Op / No Oporation)                                                                   DONE
            "01": ["Register['BC'].WriteDenary(1)"],  # LD BC d16                                                       UNSURE
            "02": ["memory.Write(Register['BC'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))"],  #         NOTEST
            "03": ["binary.Increment(Register['BC'])"],  #                                                              NOTEST
            "04": ["binary.Increment(Register['BC'], 'B')"],  #                                                         NOTEST
            "05": ["binary.Decrement(Register['BC'], 'B')"],  #                                                         NOTEST
            "06": ["Register['BC'].WriteDenary(0, 'B')"],     #                                                         NOTEST
            "07": [""],
            "08": [""],
            "09": [""],
            "0a": [""],
            "0b": [""],
            "0c": [""],
            "0d": [""],
            "0e": [""],
            "0f": [""],

            "10": ["system.Halt()"], # Stop CPU                                                                         UNSURE/UNKNOWN
            "11": ["Register['DE'].WriteDenary(0)"],  # LD BC d16                                                       UNSURE
            "12": ["memory.Write(Register['DE'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))"],  #         NOTEST
            "13": ["binary.Increment(Register['DE'])"],  #                                                              NOTEST
            "14": ["binary.Increment(Register['DE'], 'D')"],  #                                                         NOTEST
            "15": ["binary.Decrement(Register['DE'], 'D')"],  #                                                         NOTEST
            "16": ["Register['DE'].WriteDenary(0, 'D')"],     #                                                         NOTEST
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
            "21": ["Register['HL'].WriteDenary(0)"],  #                                                                 UNSURE
            "22": ["binary.Increment(Register['AF'], 'A')",
                   "memory.Write(Register['HL'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))",
                   "binary.Decrement(Register['AF'], 'A')"],  #                                                         NOTEST
            "23": ["binary.Increment(Register['HL'])"],  #                                                              NOTEST
            "24": ["binary.Increment(Register['HL'], 'H')"],  #                                                         NOTEST
            "25": ["binary.Decrement(Register['HL'], 'H')"],  #                                                         NOTEST
            "26": ["Register['HL'].WriteDenary(0, 'H')"],  #                                                            NOTEST
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
            "31": ["Register['HL'].WriteDenary(0)"],  # UNSURE
            "32": ["binary.Decrement(Register['AF'], 'A')",
                   "memory.Write(Register['HL'].ReadBinaryString(), Register['AF'].ReadBinaryString('A'))",
                   "binary.Increment(Register['AF'], 'A')"],  # NOTEST
            "33": ["binary.Increment(Register['SP'])"],  # NOTEST
            "34": ["binary.Increment(Register['HL'], 'H')"],  # NOTEST
            "35": ["binary.Decrement(Register['SP'])"],  # NOTEST
            "36": ["Register['HL'].WriteDenary(0, 'H')"],  # NOTEST
            "37": [""],
            "38": [""],
            "39": [""],
            "3a": [""],
            "3b": [""],
            "3c": [""],
            "3d": [""],
            "3e": [""],
            "3f": [""],

            "cb":["print('--------------------------------------------------------------------')"]

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