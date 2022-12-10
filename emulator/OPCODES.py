

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
            "00":["Register['B'].Set(CMD.LeftShift(Register['b'].Fetch(), 1))"],  # RLC B
        }

        self.ExtraBytes = { # How Many bytes / instructions do we need to save to what location before executing the next instruction
            "00": 0,
            "01": 2,
        }



    def ToPython(self, code):
        try:
            return "\n".join(self.CodesToPython[code])
        except KeyError:
            print("[Emulator][Decoder] Opcode not found for:", code)
            return ""