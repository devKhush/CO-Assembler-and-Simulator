from sys import stdin
import registers
import instructions

binary_to_be_generated =True

all_varaibles_defined = []   # it has all varaibles defined correctly in input file
variables = {}              # has all variables with values {'variable_Name': value_in_decimal}
variables_defination_finished = 0

all_labels_defined = []     # it has all the lables defined correctly in input file
labels = {} # {'label_Name' : address_in_decimal}

# description of the below dictionary
# all valid instructions from staring after variables to hlt
# it has all the instructions that are defined in file instructions.py as list 'instructions'
# format = {address_in_input_file :['instruction', line_no_in_input_file]}
all_instructions = {}


# reads all the instructions entered by the files
line_num = 1
halt_found = 0
current_address = 0

inp = open('input.txt')

for line in stdin:
    if line == '\n':
        line_num+=1
        continue

    instruction_entered = line.split()  #list

    if halt_found==1:
        print(f"'Syntax Error' In line no. {line_num}: 'hlt' not being used as last statement")
        binary_to_be_generated = False
        line_num+=1
        break
    
    if instruction_entered[0]=='var' and  variables_defination_finished==1:
        print(f"'Syntax Error' In line no. {line_num}: Variables NOT defined in the beginning")
        binary_to_be_generated = False
        line_num+=1

    elif instruction_entered[0]=='var':
        variable = instruction_entered[1]
        if variable in instructions.instructions:
            print(f"'Syntax Error' In line no. {line_num}: Instruction mnemonic and variables can't have same name")
            binary_to_be_generated = False
            line_num+=1
        elif variable in all_varaibles_defined:
            print(f"'Syntax Error' In line no. {line_num}: This variable is already defined")
            binary_to_be_generated = False
            line_num+=1
        elif variable in all_labels_defined:
            print(f"'Syntax Error' In line no. {line_num}: Lables and Variables can't have same name")
            binary_to_be_generated = False
            line_num+=1
        else:
            all_varaibles_defined.append(variable)
            line_num+=1

    elif instruction_entered[0][-1]==":":
        label_name = instruction_entered[0][:-1]
        if len(instruction_entered)==1:
            print(f"'Syntax Error' In line no. {line_num}: Invalid label")
            binary_to_be_generated = False
            line_num+=1
        elif  label_name in instructions.instructions:
            print(f"'Syntax Error' In line no. {line_num}: Instruction mnemonic and Labels can't have same name")
            binary_to_be_generated = False
            line_num+=1
        elif  label_name in all_labels_defined:
            print(f"'Syntax Error' In line no. {line_num}: This label is already defined")
            binary_to_be_generated = False
            line_num+=1
        elif  label_name in all_varaibles_defined:
            print(f"'Syntax Error' In line no. {line_num}: Labels and variables can't have same name")
            binary_to_be_generated = False
            line_num+=1
        elif instruction_entered[1] not in instructions.instructions:
            print(f"'Syntax Error' In line no. {line_num}: Typo in Instruction name")
            binary_to_be_generated = False
            line_num+=1
        else:
            labels[label_name] = current_address    # add 'label_name' as key in dict 'labels' with value of 'current_address'
            instruction_starts_from_index = len(instruction_entered[0]) + 1    # fetch index from which instruction starts
            all_instructions[current_address] = [line[instruction_starts_from_index :],line_num]
            variables_defination_finished = 1 
            current_address += 1 
            line_num+=1
            if instruction_entered[1]=="hlt": # label is holding hlt instruction
                halt_found==1
    
    elif instruction_entered[0] not in instructions.instructions:
        print(f"'Syntax Error' In line no. {line_num}: Typo in Instruction name")
        binary_to_be_generated = False
        line_num+=1
    
    elif instruction_entered[0] in instructions.instructions:
        variables_defination_finished =1
        all_instructions[current_address] = [line,line_num]
        line_num+=1
        current_address +=1
        if instruction_entered[0]=="hlt":
            halt_found=1

if halt_found==0:
    print(f"'Syntax Error' In line no. {line_num}: Missing 'hlt' instruction")
    binary_to_be_generated = False

if current_address>256:
    print(f"'General Syntax Error' In line no. {line_num}: More than 256 instructions encountered")
    binary_to_be_generated = False

if binary_to_be_generated:
    for variableName in all_varaibles_defined:
        variables[variableName] = current_address
        current_address+=1


if binary_to_be_generated:
    program_counter = 0
    while program_counter < len(all_instructions.keys()):
        
    #for address,list in all_instructions.items():    # ignore this
        instruction_to_be_executed = all_instructions[program_counter][0].split()
        line_num = all_instructions[program_counter][1]
        
        if instruction_to_be_executed[0] in instructions.type_A_instructions:
            if len(instruction_to_be_executed)!=4:
                print(f"'Syntax Error' In line no. {line_num}: Wrong syntax used for Type-A instructions")
                quit()

            elif (instruction_to_be_executed[1] not in registers.binary_of_registers.keys()) or (instruction_to_be_executed[2] not in registers.binary_of_registers.keys()) or (instruction_to_be_executed[3] not in registers.binary_of_registers.keys()):
                print(f"'Syntax Error' In line no. {line_num }: Register not supported by ISA")
                quit()
            registers.typeA_fun(instruction_to_be_executed)
        

        elif (instruction_to_be_executed[0] in instructions.type_B_instructions) and (instruction_to_be_executed[0]!='mov'):
            if len(instruction_to_be_executed)!=3:
                print(f"'Syntax Error' In line no. {line_num }: Wrong syntax used for Type-B instructions")
                quit()
            elif instruction_to_be_executed[2][0]!='$' or ( not instruction_to_be_executed[2][1:].isdecimal()):
                print(f"'Syntax Error' In line no. {line_num }: Wrong syntax used for Type-B instructions")
                quit()
            elif (instruction_to_be_executed[1] not in registers.binary_of_registers.keys()):
                print(f"'Syntax Error' In line no. {line_num }: Register not supported by ISA")
                quit()
            elif ( int(instruction_to_be_executed[2][1:])>255 or int(instruction_to_be_executed[2][1:])<0):
                print(f"'Syntax Error' In line no. {line_num }: Immediate value out of Range")
                quit()
            instructions.typeB_fun(instruction_to_be_executed)
        

        elif (instruction_to_be_executed[0] in instructions.type_C_instructions) and (instruction_to_be_executed[0]!='mov'):
            if len(instruction_to_be_executed)!=3:
                print(f"'Syntax Error' In line no. {line_num }: Wrong syntax used for Type-C instructions")
                quit()

            elif (instruction_to_be_executed[1] not in registers.binary_of_registers.keys()) or (instruction_to_be_executed[2] not in registers.binary_of_registers.keys()):
                print(f"'Syntax Error' In line no. {line_num }: Register not supported by ISA")
                quit()
            instructions.typeC_fun(instruction_to_be_executed)

        
        elif instruction_to_be_executed[0]=='mov':
            if instruction_to_be_executed[2][0]=='$':
                if len(instruction_to_be_executed)!=3:
                    print(f"'Syntax Error' In line no. {line_num }: Wrong syntax used for Type-B instructions")
                    quit()
                elif instruction_to_be_executed[2][0]!='$' or ( not instruction_to_be_executed[2][1:].isdecimal()):
                    print(f"'Syntax Error' In line no. {line_num }: Wrong syntax used for Type-B instructions")
                    quit()
                elif (instruction_to_be_executed[1] not in registers.binary_of_registers.keys()):
                    print(f"'Syntax Error' In line no. {line_num }: Register not supported by ISA")
                    quit()
                elif (int(instruction_to_be_executed[2][1:])>255 or int(instruction_to_be_executed[2][1:])<0):
                    print(f"'Syntax Error' In line no. {line_num }: Immediate value out of Range")
                    quit()
                instructions.typeB_fun(instruction_to_be_executed)
            else:
                if len(instruction_to_be_executed)!=3:
                    print(f"'Syntax Error' In line no. {line_num }: Wrong syntax used for Type-C instructions")
                    quit()

                elif (instruction_to_be_executed[1] not in registers.binary_of_registers.keys()) or (instruction_to_be_executed[2] not in registers.binary_of_registers.keys()):
                    print(f"'Syntax Error' In line no. {line_num }: Register not supported by ISA")
                    quit()
                elif (instruction_to_be_executed[1] not in registers.binary_of_registers.keys()) or (instruction_to_be_executed[2] not in registers.flags.keys()):
                    print(f"'Syntax Error' In line no. {line_num }: Register not supported by ISA")
                    quit()
                instructions.typeC_fun(instruction_to_be_executed)


        elif instruction_to_be_executed[0] in instructions.type_D_instructions:
            if len(instruction_to_be_executed)!=3:
                print(f"'Syntax Error' In line no. {line_num }: Wrong syntax used for Type-D instructions")
                quit()
            elif instruction_to_be_executed[1] not in registers.binary_of_registers.keys():
                print(f"'Syntax Error' In line no. {line_num }: Register not supported by ISA")
                quit()
            elif instruction_to_be_executed[2] not in all_varaibles_defined:
                print(f"'Syntax Error' In line no. {line_num }: Variable '{instruction_to_be_executed[2]}' not defined")
                quit()
            registers.typeD_fun(instruction_to_be_executed)


        elif instruction_to_be_executed[0] in instructions.type_E_instructions:
            if len(instruction_to_be_executed)!=2:
                print(f"'Syntax Error' In line no. {line_num }: Wrong syntax used for Type-E instructions")
                quit()
            elif (instruction_to_be_executed[1] not in all_labels_defined):
                print(f"'Syntax Error' In line no. {line_num }: Label '{instruction_to_be_executed[1]}' not defined")
                quit()
            program_counter = registers.typeE_fun(instruction_to_be_executed,program_counter)


        elif instruction_to_be_executed in instructions.type_F_instructions:
            instructions.typeF_fun(instruction_to_be_executed)
        
        program_counter+=1
