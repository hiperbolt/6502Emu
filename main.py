class CPU:
    """
    CPU Object 
            """
    def __init__(self) -> None:
        CPU.reset()

    def reset(self): 
        self.PC = 0     # Program Counter Register
        
        self.SP = 0xff  # Initialize Stack Pointer

        self.A = 0      # Acumulator Register

        self.X = 0      # X register
        self.Y = 0      # Y Register

        self.PS = 32     # Set Processor Status to 32 (Only value that doesn't have a meaning.)

        """
        Each flag has a single bit within the register. Negative flag is binary 10000000 -> decimal 128
        Using decimal and converting to binary when needed.
        """
        self.PSFlags = {
            'N': 128,   # Negative
            'V': 64,    # Overflow
            'B': 16,    # Break Command
            'D': 8,     # Decimal Mode
            'I': 4,     # IRQ Disable
            'Z': 2,     # Zero
            'C': 1      # Carry
        }

    def setFlag(self, flag):
        self.PS = self.PS + self.PSFlags[flag]   # Adds flag value (in decimal)

    def clearFlag(self, flag):
        self.PS = self.PS - self.PSFlags[flag]   # Remove flag's value (In decimal)

    def clearFlags(self):
        self.PS = 32    # Resets Processor Status Register

    #def getFlags(self):
    #    self.PS

