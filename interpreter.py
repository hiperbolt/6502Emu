import cpu
import memory

c = cpu.CPU()
m = memory.Mem()

logging = True

'''
Addressing Modes:

'Implicit' - no further operand needs to be specified
'Accumulator' - option to operate directly upon the accumulator
'Immediate' - Immediate addressing allows the programmer to directly specify an 8 bit constant within the instruction.




'''

### LOAD/STORE OPERATIONS

def LDA(mode, arg):      # Load Accumulator - 8 moded / Sets either N or Z flag
    if mode == "Immediate":
        constant = arg
        c.A = constant
    
    if mode == "Zero Page":
        eightbitaddress = arg
        c.A = m.get(eightbitaddress)
    
    if mode == "Zero Page, X":
        eightbitaddress = arg
        c.A = m.get(eightbitaddress) + c.X

    if mode == "Absolute":
        fulladdress = arg
        c.A = m.get(fulladdress)

    if mode == "Absolute, X":
        fulladdress = arg
        c.A = m.get(fulladdress) + c.X
    
    if mode == "Absolute, Y":
        fulladdress = arg
        c.A = m.get(fulladdress) + c.Y

    if mode == "Indirect, X":
        pass

    if mode == "Indirect, Y":
        pass

    ### Setting flags
    if c.A == 0:    # If Accumulator is 0, set Z flag
        c.setFlag('Z')

    if (int(format(c.A, '08b')) & 0b1000000):   # If 0b1000000 evaluates to true (If 7th bit is set, as per instruction set) set N flag
        c.setFlag('N')


def LDX(mode, arg):      # Load X Register - 5 moded / Sets either N or Z flag
    if mode == "Immediate":
        constant = arg
        c.X = constant
    
    if mode == "Zero Page":
        eightbitaddress = arg
        c.X = m.get(eightbitaddress)

    if mode == "Zero Page, Y":
        eightbitaddress = arg
        c.X = m.get(eightbitaddress) + c.Y

    if mode == "Absolute":
        fulladdress = arg
        c.X = m.get(fulladdress)

    if mode == "Absolute, Y":
        fulladdress = arg
        c.X = m.get(fulladdress) + c.Y
    

    ### Settings flags
    if c.X == 0:    # If Accumulator is 0, set Z flag
        c.setFlag('Z')

    if (int(format(c.X, '08b')) & 0b1000000):   # If 0b1000000 evaluates to true (If 7th bit is set, as per instruction set) set N flag
        c.setFlag('N')

def LDY(mode, arg):      # Load Y Register - 5 moded / Sets either N or Z flag
    if mode == "Immediate":
        constant = arg
        c.Y = constant
    
    if mode == "Zero Page":
        eightbitaddress = arg
        c.Y = m.get(eightbitaddress)

    if mode == "Zero Page, X":
        eightbitaddress = arg
        c.Y = m.get(eightbitaddress) + c.X

    if mode == "Absolute":
        fulladdress = arg
        c.Y = m.get(fulladdress)

    if mode == "Absolute, Y":
        fulladdress = arg
        c.Y = m.get(fulladdress) + c.X
    

    ### Settings flags
    if c.Y == 0:    # If Accumulator is 0, set Z flag
        c.setFlag('Z')

    if (int(format(c.Y, '08b')) & 0b1000000):   # If 0b1000000 evaluates to true (If 7th bit is set, as per instruction set) set N flag
        c.setFlag('N')

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

def SEC():      # Set Carry flag - Implicit. 
    c.setFlag('C')
    if logging == True:
        print('Set Carry flag called')

def SED():      # Set Decimal mode flag - Implicit. 
    c.setFlag('D')
    if logging == True:
        print('Set Decimal mode flag called')

def SEI():      # Set Interrupt Disable flag - Implicit. 
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
