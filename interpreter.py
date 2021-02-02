import cpu
import memory

c = cpu.CPU()
m = memory.Mem()

logging = True

### LOAD/STORE OPERATIONS

def LDA(mode):      # Load Accumulator - 8 moded / Sets either N or Z flag
    pass

def LDX(mode):      # Load X Register - 5 moded / Sets either N or Z flag
    pass

def LDY(mode):      # Load Y Register - 5 moded / Sets either N or Z flag
    pass

def STA(mode):      # Store Accumulator - 8 moded
    pass

def STX(mode):      # Store X Register - 3 moded
    pass

def STY(mode):      # Store Y Register - 3 moded
    pass



#### STATUS FLAG CHANGES

def CLC():      # Clear Carry flag - Implicit
    c.clearFlag('C')
    if logging == True:
        print('Clear Carry Flag called')

def CLD():      # Clear Decimal Mode flag - Implicit
    c.clearFlag('D')
    if logging == True:
        print('Clear decimal mode flag called')

def CLI():      # Clear Interrupt disable flag - Implicit
    c.clearFlag('I')
    if logging == True:
        print('Clear Interrupt Disable flag called')

def CLV():      # Clear Overflow flag - Implicit
    c.clearFlag('V')
    if logging == True:
        print('Clear Overflow flag called')

def SEC(flag):      # Set Carry flag - Implicit. Recieves flag as argument (Listing on cpu.py)
    c.setFlag('C')
    if logging == True:
        print('Set Carry flag called')

def SED(flag):      # Set Decimal mode flag - Implicit. Recieves flag as argument (Listing on cpu.py)
    c.setFlag('C')
    if logging == True:
        print('Set Carry flag called')

def SEI(flag):      # Set Interrupt Disable flag - Implicit. Recieves flag as argument (Listing on cpu.py)
    c.setFlag('I')
    if logging == True:
        print('Set Interrupt disable called')


#### SYSTEM FUNCTIONS
def BRK():      # Break operation - Implicit
    pass        # WIP


def NOP():      # No Operation - Implicit
    if logging == True:
        print('NOP called')

def RTI():      # Return from Interrupt - Implicit
    pass        # WIP
