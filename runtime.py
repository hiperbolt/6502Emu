import argparse
import sys

import cpu
import memory
import instructions

c = cpu.CPU()                           #### Initializing CPU instance.
m = memory.Mem()                        #### Initializing Mem instance.
i = instructions.Instructions(c, m)     #### Initializing Instructions instance and passing CPU and Mem instance.

parser = argparse.ArgumentParser(description='Runtime for hiperbolt\'s 6502ad Emulator.')

parser.add_argument('-f', help='File mode - Interpret a binary 6502ad file.')
parser.add_argument('-b', help='Binary mode - For Raspberry Pi only.')

args = parser.parse_args()

def exitShell():
    print("Exiting.\n")
    exit()

def peekMem(address):
    print("Byte at address" + str(address) + ": "+ str(m.get(address)))

customCallsMap = { 'peekMem' : peekMem, 'exit' : exitShell}


if not (len(sys.argv) > 1):     #### Interpreted mode
    print("Welcome to hiperbolt's 6502ad Emu interactive mode.\n")
    while 1:
        command = input('> ')
        if command in customCallsMap:
            if command == 'exit':
                exitShell()

        else:
            inst = ('i.' + command)
            exec(str(inst))






