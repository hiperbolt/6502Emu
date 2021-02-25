import cpu
import memory

c = cpu.CPU()
m = memory.Mem()

def stackPush(value):
    m.put(c.SP, int(value))
    c.SP -= 1

print(c.SP)
stackPush(12)
print(c.SP)