

class Codes():
    def __init__(self):
        self.CodesToPython = {
            "00": [""],  # NOP (No-Op / No Oporation)               DONE
            "01": [""],  # LD BC d16 (Move a value from A to B)
            "02": [""],  #
            "03": [""],  #
            "04": [""],  #
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