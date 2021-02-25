import cpu
import memory

c = cpu.CPU()
m = memory.Mem()

def funcReturns(x) -> int:
    return x+1

def funcDoes(x, y) -> None:
    a = 1+5
    print('')
    

if funcReturns(1):
    print("1")

if funcDoes(1, 2):
    print("oh nos")