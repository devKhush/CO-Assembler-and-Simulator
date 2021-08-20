from sys import stdin


class Memory:
    def __init__(self):
        self.memoryDict = {}  # {pc : instruction_binary_code}

    def getData(self, pc):
        instruction = self.memoryDict[pc]
        return instruction

class Program_counter:
    def __init__(self):
        self.pc_value=0

    def dump(self):
        pc_binary = '{0:08b}'.format(self.pc_value)
        print(pc_binary, end=" ")

    def update(self,new_pc):
        self.pc_value = new_pc


class Registers:
    all_registers = {'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0}
    flags = '011'
    LGE = 0
    V = 0

    def dump(self):
        r0_binary = '{0:016b}'.format(self.all_registers['R0'])
        r1_binary = '{0:016b}'.format(self.all_registers['R1'])
        r2_binary = '{0:016b}'.format(self.all_registers['R2'])
        r3_binary = '{0:016b}'.format(self.all_registers['R3'])
        r4_binary = '{0:016b}'.format(self.all_registers['R4'])
        r5_binary = '{0:016b}'.format(self.all_registers['R5'])
        r6_binary = '{0:016b}'.format(self.all_registers['R6'])
        flag_binary = '0'*12 + str(self.V)+ str(self.LGE)
        print(r0_binary,end=" "), print(r1_binary,end =" "), print


def initialize(memoryDict):
    address = 0
    for line in stdin:
        memoryDict[address] = line
        address += 1


memory = Memory()
initialize(memory.memoryDict)     # Load memory from stdin
PC = Program_counter()            # initialise the pc and Start from the first 0th instruction
register = Registers()

halted = False
while not halted:
    Instruction = memory.getData(PC)          # Get current instruction
    halted, new_PC = EE.execute(Instruction)  # Update RF compute new_PC
    PC.dump()                                 # Print PC
    register.dump()                                 # Print RF state
    PC.update(new_PC)  # Update PC

memory.dump()
