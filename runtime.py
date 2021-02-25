import argparse
import sys
import re

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
    print("Byte at address " + str(address) + ": "+ str(m.get(address)))


def reset():
    m.reset()
    print("RESET: Memory flushed.")
    c.reset()
    print("RESET: Registers flushed.")
    print("RESET: Done.")
    

customCalls = { 'peekMem', 'exit', 'reset'}


if not (len(sys.argv) > 1):     #### Interpreted mode
    print("Welcome to hiperbolt's 6502ad Emu interactive mode.\n")
    while 1:
        command = input('> ').split()

        if command[0] in customCalls:
            if command[0] == 'exit':
                exitShell()
            if command[0] == 'peekMem':
                try:
                    peekMem(int(command[1]))
                except IndexError:
                    print("ERROR: Missing arguments.")
            if command[0] == 'reset':
                reset()

        else:
            inst = ('i.' + command[0])
            try:
                exec(str(inst))
            except AttributeError:
                print("ERROR: Command does not exist.")
            #except SyntaxError:
            #    print("ERROR: Bad syntax.")
            #except TypeError:
            #    print("ERROR: Bad arguments.")




