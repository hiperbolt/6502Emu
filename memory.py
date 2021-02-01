class Mem:
    def __init__(self) -> None:
        Mem.reset(self)      # Calls function to fill the entire memory buffer with 0's

    def reset(self):
        self.memory = ["00000000"] * 65000     # Fills the entire memory buffer with 0's

    def get(self, address) -> str:
        decimalAddress = str(int(address,16))   # Converts hexadecimal address in decimal address
        return self.memory[address]

    def put(self, address, value):
        decimalAddress = str(int(address,16))   # Converts hexadecimal address in decimal address
        self.memory[address] = value