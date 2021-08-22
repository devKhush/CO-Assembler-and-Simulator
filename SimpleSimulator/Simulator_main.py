from sys import stdin


class Memory:
    def __init__(self):
        self.memoryDict = {}  # {pc : instruction_binary_code}

    def fetch(self, pc):
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
    all_registers = {'000':0,'001':0,'010':0,'011':0,'100':0,'101':0,'110':0}
    flags = '111'
    LGE = 0
    V = 0

    def dump(self):
        r0_binary = '{0:016b}'.format(self.all_registers['000'])
        r1_binary = '{0:016b}'.format(self.all_registers['001'])
        r2_binary = '{0:016b}'.format(self.all_registers['010'])
        r3_binary = '{0:016b}'.format(self.all_registers['011'])
        r4_binary = '{0:016b}'.format(self.all_registers['100'])
        r5_binary = '{0:016b}'.format(self.all_registers['101'])
        r6_binary = '{0:016b}'.format(self.all_registers['110'])
        flag_binary = '0'*12 + str(self.V)+ str(self.LGE)
        print(r0_binary,end=" "), print(r1_binary,end =" "), print(r2_binary,end=" "), print(r3_binary,end =" ")
        print(r4_binary,end=" "), print(r5_binary,end=" "), print(r6_binary,end=" "), print(flag_binary)



def initialize(memory_dict):
    address = 0
    for line in stdin:
        memory_dict[address] = line
        address += 1


def showTraces():
    #to be done by Khushdev for bonus
    return


def dumpMemory(programMemory, variableMemory):
    lines = 1
    for i,j in programMemory.items():
        print(j)
        lines+=1
    for i,j in variableMemory.items():
        variable_value_in_binary = '{0:016b}'.format(j)
        print(variable_value_in_binary)
        lines+=1
    while lines<=256:
        print('0'*16)
        lines+=1
    return


def execute(instruction, pc, register, programMemory, variableMemory):
    # divide work among them equally
    # add code for this function
    opcode = instruction[0:5]    # opcode of instruction

    if opcode=='10011':               # halt instruction
        return True, pc

    elif opcode=='00100':            # load instruction
        variable_address = instruction[8:]
        register_operand = instruction[5:8]
        if variable_address in variableMemory.keys():
            register.all_registers[register_operand] = variableMemory[variable_address]
            return False, pc+1
        else:
            variableMemory[variable_address] = 0
            register.all_registers[register_operand] = variableMemory[variable_address]
            return False, pc+1

    elif opcode == '00101':              # store instruction
        variable_address = instruction[8:]
        register_operand = instruction[5:8]
        if variable_address in variableMemory.keys():
            variableMemory[variable_address] = register.all_registers[register_operand]
            return False, pc+1
        else:
            variableMemory[variable_address] = 0
            variableMemory[variable_address] = register.all_registers[register_operand]
            return False, pc+1

    elif opcode == '00000':

        reg1 = instruction[7:10]
        reg2 = instruction[10:13]
        reg3 = instruction[13:]

        reg2_val = register.all_registers[reg2]
        reg3_val = register.all_registers[reg3]

        s = reg2_val + reg3_val

        if s > pow(2,16) - 1:
            register.V = 1
            register.all_registers[reg1] = s - pow(2,16)
        else:
            register.all_registers[reg1] = s
        
        return False, pc+1
    
    elif opcode == '00001':

        reg1 = instruction[7:10]
        reg2 = instruction[10:13]
        reg3 = instruction[13:]

        reg2_val = register.all_registers[reg2]
        reg3_val = register.all_registers[reg3]

        s= reg2_val-reg3_val

        if s<0:
            register.V=1
        else:
            register.all_registers[reg1] = s
        
        return False, pc+1

    elif opcode == '00110':

        reg1 = instruction[7:10]
        reg2 = instruction[10:13]
        reg3 = instruction[13:]

        reg2_val = register.all_registers[reg2]
        reg3_val = register.all_registers[reg3]

        s= reg2_val*reg3_val

        if s>pow(2,16) - 1:
            register.V=1
        else:
            register.all_registers[reg1] = s
        
        return False, pc+1
        
    
    return



variable_memory = {} # stores all the variable encountered in format {'address_in_binary_string' : value_in_decimal}
memory = Memory()       # object of Memory, see implementation. It has a dict 'memory.memoryDict' which stores {address_in_decimal : 'instruction_in_16_bit_binary_as_string'}
initialize(memory.memoryDict)     # Load memory from stdin
PC = Program_counter()            # initialise the pc and Start from the first 0th instruction
register = Registers()            # object of Registers, see implementation

halted = False
while not halted:
    Instruction = memory.fetch(PC)                   # Get current instruction
    halted, new_PC = execute(Instruction, PC.pc_value, register, memory.memoryDict, variable_memory) # Update Registers and compute new_PC
    PC.dump()                                          # Print PC
    register.dump()                                    # Print Register's state
    PC.update(new_PC)  # Update PC

dumpMemory(memory.memoryDict, variable_memory)
showTraces()