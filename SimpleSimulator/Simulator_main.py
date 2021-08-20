from sys import stdin

class Memory:
    def __init__(self):
        self.memoryDict = {}       # {pc : instruction_binary_code}

    def getData(self,pc):
        instruction = self.memoryDict



def initialize(memory):
    address = 0
    for line in stdin:
        memory[address] = line
        address+=1









memory = Memory()
initialize(memory) # Load memory from stdin
PC = 0             # Start from the first instruction
halted = False
while not halted:
    Instruction = memory.getData(PC)          # Get current instruction
    halted, new_PC = EE.execute(Instruction)  # Update RF compute new_PC
    PC.dump()                                 # Print PC
    RF.dump()                                 # Print RF state
    PC.update(new_PC)                         # Update PC


memory.dump() 