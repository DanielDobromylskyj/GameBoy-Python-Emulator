

class Codes():
    def __init__(self):
        self.CodesToPython = {
            "00": [""],  # NOP (No-Op / No Oporation)               DONE
            "01": [""],  # LD BC d16 (Move a value from A to B)
            "02": [""],  #
            "03": [""],  #
            "04": [""],  #
        }

        self.ExtraBytes = { # How Many bytes / instructions do we need to save to what location before executing the next instruction
            "00": None,
            "01": 2,
        }

    def ToPython(self, code):
        return "\n".join(self.CodesToPython[code])