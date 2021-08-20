initialize(memory) # Load memory from stdin
PC = 0             # Start from the first instruction
halted = False
white(not halted):
    Instruction = memory.getData(PC)             # Get current instruction
    halted, new_PC = EE.execute(Instruction)  # Update RF compute new_PC
    PC.dump()                                 # Print PC
    RF.dump()                                 # Print RF state
    PC.update(new_PC)                         # Update PC


memory.dump() 