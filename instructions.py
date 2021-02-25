logging = True

### LOAD/STORE OPERATIONS

class Instructions:
    def __init__(self, cpuObject, memObject) -> None:
        self.c = cpuObject
        self.m = memObject

    def LDA(self, mode, arg):      # Load Accumulator - 8 moded / Sets either N or Z flag
        if mode == "Immediate":
            constant = arg
            self.c.A = constant

        if mode == "Zero Page":
            eightbitaddress = arg
            self.c.A = self.m.get(eightbitaddress)

        if mode == "Zero Page, X":
            eightbitaddress = arg
            self.c.A = self.m.get(eightbitaddress) + self.c.X

        if mode == "Absolute":
            fulladdress = arg
            self.c.A = self.m.get(fulladdress)

        if mode == "Absolute, X":
            fulladdress = arg
            self.c.A = self.m.get(fulladdress) + self.c.X

        if mode == "Absolute, Y":
            fulladdress = arg
            self.c.A = self.m.get(fulladdress) + self.c.Y

        if mode == "Indirect, X":
            pass

        if mode == "Indirect, Y":
            pass

        ### Setting flags
        if self.c.A == 0:    # If Accumulator is 0, set Z flag
            self.c.setFlag('Z')

        if (int(format(self.c.A, '08b')) & 0b1000000):   # If 0b1000000 evaluates to true (If 7th bit is set, as per instruction set) set N flag
            self.c.setFlag('N')


    def LDX(self, mode, arg):      # Load X Register - 5 moded / Sets either N or Z flag
        if mode == "Immediate":
            constant = arg
            self.c.X = constant

        if mode == "Zero Page":
            eightbitaddress = arg
            self.c.X = self.m.get(eightbitaddress)

        if mode == "Zero Page, Y":
            eightbitaddress = arg
            self.c.X = self.m.get(eightbitaddress) + self.c.Y

        if mode == "Absolute":
            fulladdress = arg
            self.c.X = self.m.get(fulladdress)

        if mode == "Absolute, Y":
            fulladdress = arg
            self.c.X = self.m.get(fulladdress) + self.c.Y


        ### Settings flags
        if self.c.X == 0:    # If Accumulator is 0, set Z flag
            self.c.setFlag('Z')

        if (int(format(self.c.X, '08b')) & 0b1000000):   # If 0b1000000 evaluates to true (If 7th bit is set, as per instruction set) set N flag
            self.c.setFlag('N')

    def LDY(self, mode, arg):      # Load Y Register - 5 moded / Sets either N or Z flag
        if mode == "Immediate":
            constant = arg
            self.c.Y = constant

        if mode == "Zero Page":
            eightbitaddress = arg
            self.c.Y = self.m.get(eightbitaddress)

        if mode == "Zero Page, X":
            eightbitaddress = arg
            self.c.Y = self.m.get(eightbitaddress) + self.c.X

        if mode == "Absolute":
            fulladdress = arg
            self.c.Y = self.m.get(fulladdress)

        if mode == "Absolute, Y":
            fulladdress = arg
            self.c.Y = self.m.get(fulladdress) + self.c.X


        ### Setting flags
        if self.c.Y == 0:    # If Accumulator is 0, set Z flag
            self.c.setFlag('Z')

        if (int(format(self.c.Y, '08b')) & 0b1000000):   # If 0b1000000 evaluates to true (If 7th bit is set, as per instruction set) set N flag
            self.c.setFlag('N')

    def STA(self, mode, arg):      # Store Accumulator - 7 moded
        if mode == "Zero Page":
            eightbitaddress = arg
            self.m.put(eightbitaddress, int(self.c.A))

        if mode == "Zero Page, X":
            eightbitaddress = arg
            self.m.put(eightbitaddress, (int(self.c.A) + self.c.X))

        if mode == "Zero Page, Y":
            eightbitaddress = arg
            self.m.put(eightbitaddress, (int(self.c.A) + self.c.Y))

        if mode == "Absolute":
            fulladdress = arg
            self.m.put(fulladdress)

        if mode == "Absolute, X":
            fulladdress = arg
            self.c.X = self.m.get(fulladdress) + self.c.Y

        if mode == "Absolute, Y":
            fulladdress = arg
            self.c.Y = self.m.get(fulladdress) + self.c.X

        if mode == "Indirect, X":
            pass
        
        if mode == "Indirect, Y":
            pass
        


    def STX(self, mode, arg):      # Store X Register - 3 moded
        if mode == "Zero Page":
            eightbitaddress = arg
            self.m.put(eightbitaddress, int(self.c.X))

        if mode == "Zero Page, Y":
            eightbitaddress = arg
            self.m.put(eightbitaddress, (int(self.c.X) + self.c.Y))

        if mode == "Absolute":
            fulladdress = arg
            self.m.put(fulladdress, int(self.c.Y))


    def STY(self, mode, arg):      # Store Y Register - 3 moded
        if mode == "Zero Page":
            eightbitaddress = arg
            self.m.put(eightbitaddress, int(self.c.Y))

        if mode == "Zero Page, X":
            eightbitaddress = arg
            self.m.put(eightbitaddress, (int(self.c.Y) + self.c.X))

        if mode == "Absolute":
            fulladdress = arg
            self.m.put(fulladdress, int(self.c.Y))

    #### REGISTER TRANSFERS

    def TAX(self):       # Transfer accumulator to X - Implicit
        self.c.X = self.c.A

    def TAY(self):       # Transfer accumulator to Y - Implicit
        self.c.Y = self.c.A

    def TXA(self):       # Transfer X to accumulator - Implicit
        self.c.A = self.c.X

    def TYA(self):       # Transfer Y to accumulator - Implicit
        self.c.A = self.c.Y

    #### STACK OPERATIONS

    ### Stack Implementation
    #   The stack exists from $0100 to $01FF (256-511) on memory.
    #   The Stack Pointer (SP) points to the next free byte of memory (where the next value will be stored).
    #   Therefore, the pointer is moved *after* pushing, and *before* pulling.
    #   The stack grows downwards.

    def stackPush(self, value):
        self.m.put(self.c.SP, int(value))
        self.c.SP -= 1

    def stackPull(self) -> int:
        self.c.SP += 1
        toReturn = int(self.m.get(self.c.SP))
        self.m.put(self.c.SP, int(0))
        print(toReturn) #Temporary fix
        return toReturn


    def TSX(self):      # Transfer Stack Pointer to X - Implicit - Sets N or Z
        self.c.X = self.c.SP

        ### Setting flags
        if self.c.X == 0:    # If Accumulator is 0, set Z flag
            self.c.setFlag('Z')

        if (int(format(self.c.X, '08b')) & 0b1000000):   # If 0b1000000 evaluates to true (If 7th bit is set, as per instruction set) set N flag
            self.c.setFlag('N')


    def TXS(self):   # Transfer X to Stack Pointer - Implicit
        self.c.SP = self.c.X

    def PHA(self):
        self.stackPush(self.c.A)


    def PHP(self):
        self.stackPush(self.c.PS)


    def PLA(self):
        self.c.A = self.stackPull()

        ### Setting flags
        if self.c.X == 0:    # If Accumulator is 0, set Z flag
            self.c.setFlag('Z')

        if (int(format(self.c.X, '08b')) & 0b1000000):   # If 0b1000000 evaluates to true (If 7th bit is set, as per instruction set) set N flag
            self.c.setFlag('N')


    def PLP(self):
        self.c.PS = self.stackPull() 



    #### STATUS FLAG CHANGES

    def CLC(self):      # Clear Carry flag - Implicit
        self.c.clearFlag('C')
        if logging == True:
            print('Clear Carry Flag called')

    def CLD(self):      # Clear Decimal Mode flag - Implicit
        self.c.clearFlag('D')
        if logging == True:
            print('Clear decimal mode flag called')

    def CLI(self):      # Clear Interrupt disable flag - Implicit
        self.c.clearFlag('I')
        if logging == True:
            print('Clear Interrupt Disable flag called')

    def CLV(self):      # Clear Overflow flag - Implicit
        self.c.clearFlag('V')
        if logging == True:
            print('Clear Overflow flag called')

    def SEC(self):      # Set Carry flag - Implicit. 
        self.c.setFlag('C')
        if logging == True:
            print('Set Carry flag called')

    def SED(self):      # Set Decimal mode flag - Implicit. 
        self.c.setFlag('D')
        if logging == True:
            print('Set Decimal mode flag called')

    def SEI(self):      # Set Interrupt Disable flag - Implicit. 
        self.c.setFlag('I')
        if logging == True:
            print('Set Interrupt disable called')


    #### SYSTEM FUNCTIONS
    def BRK(self):      # Break operation - Implicit
        pass        # WIP


    def NOP(self):      # No Operation - Implicit
        if logging == True:
            print('NOP called')

    def RTI(self):      # Return from Interrupt - Implicit
        pass        # WIP