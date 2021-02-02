class CPU:
    """
    CPU Object 
            """
    def __init__(self) -> None:
        CPU.reset(self)

    def reset(self):        # Hard-coded types because python handles types in an annoying way.
        self.PC = int(0)    # Program Counter Register 
        
        self.SP = int(256)  # Initialize Stack Pointer

        self.A = int(0)     # Acumulator Register

        self.X = int(0)     # X register
        self.Y = int(0)     # Y Register

        self.PS = int(0)    # 0 doesn't have a flag value

        """
        Each flag has a single bit within the register. Negative flag is binary 10000000 -> decimal 128
        Using decimal and converting to binary when needed.
        """
        self.PSFlags = {
            'N': 128,   # Negative
            'V': 64,    # Overflow
            'B': 16,    # Break Command
            'D': 8,     # Decimal Mode
            'I': 4,     # Interrupt Disable
            'Z': 2,     # Zero
            'C': 1      # Carry
        }

    def setFlag(self, flag):
        self.PS = self.PS + self.PSFlags[flag]   # Adds flag value (in decimal)

    def clearFlag(self, flag):
        if self.PS > 0:                              # Remove flag only if there are flags to remove (Value of PS is 0 if no flags are set)
            self.PS = self.PS - self.PSFlags[flag]   # Remove flag's value (In decimal)

    def clearFlags(self):
        self.PS = 32    # Resets Processor Status Register

    #def getFlags(self):
    #    self.PS

