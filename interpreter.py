import cpu
import memory

c = cpu.CPU()
m = memory.Mem()

logging = True

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
        print('clear overflow flag called')

def SEC(flag):      # Set Carry flag - Implicit. Recieves flag as argument (Listing on cpu.py)
    c.setFlag(flag)

#### SYSTEM FUNCTIONS

def NOP():      # No Operation - Implicit
    if logging == True:
        print('NOP called')

