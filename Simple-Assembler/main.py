from sys import stdin
import registers
import instructions

all_varaibles_defined = []   # it has all varaibles defined correctly in input file
variables = {}              # has all variables with values {'variable_Name': value_in_decimal}
variables_defination_finished = 0

all_labels_defined = []     # it has all the lables defined correctly in input file
labels = {} # {'lable_Name' : address_in_decimal}

# description of the below dictionary
# all valid instructions from staring after variables to hlt
# it has all the instructions that are defined in file instructions.py as list 'instructions'
# format = {address_in_input_file :['instruction', line_no_in_input_file]}
all_instructions = {}


# reads all the instructions entered by the files
line_num = 1
halt_found = 0
current_address = 0

for line in stdin:
    if line == '':
        line_num+=1
        continue

    instruction_entered = line.split()  #list

    if halt_found==1:
        print(f"'Syntax Error' In line no. {line_num}: 'hlt' not being used as last statement")
        line_num+=1
        break
    
    if instruction_entered[0]=='var' and  variables_defination_finished==1:
        print(f"'Syntax Error' In line no. {line_num}: Variables NOT defined in the beginning")
        line_num+=1

    elif instruction_entered[0]=='var':
        variable = instruction_entered[1]
        if variable in instructions.instructions:
            print(f"'Syntax Error' In line no. {line_num}: Instruction mnemonic and variables can't have same name")
            line_num+=1
        elif variable in all_varaibles_defined:
            print(f"'Syntax Error' In line no. {line_num}: This variable is already defined")
            line_num+=1
        elif variable in all_labels_defined:
            print(f"'Syntax Error' In line no. {line_num}: Lables and Variables can't have same name")
            line_num+=1
        else:
            all_varaibles_defined.append(variable)
            line_num+=1

    elif instruction_entered[0][-1]==":":
        label_name = instruction_entered[0][:-1]
        if  label_name in instructions.instructions:
            print(f"'Syntax Error' In line no. {line_num}: Instruction mnemonic and Labels can't have same name")
            line_num+=1
        elif  label_name in all_labels_defined:
            print(f"'Syntax Error' In line no. {line_num}: This label is already defined")
            line_num+=1
        elif  label_name in all_varaibles_defined:
            print(f"'Syntax Error' In line no. {line_num}: Labels and variables can't have same name")
            line_num+=1
        else:
            labels[label_name] = current_address    # add 'label_name' as key in dict 'labels' with value of 'current_address'
            instruction_starts_from_index = len(instruction_entered[0]) + 1    # fetch index from which instruction starts
            all_instructions[current_address] = line[instruction_starts_from_index :]
            variables_defination_finished = 1 
            current_address += 1 
            if instruction_entered[1]=="hlt": # label is holding hlt instruction
                halt_found==1
    
    elif instruction_entered[0] not in instructions.instructions:
        print(f"'Syntax Error' In line no. {line_num}: Typo in Instruction name")
        line_num+=1
    
    elif instruction_entered[0] in instructions.instructions:
        variables_defination_finished =1
        all_instructions[current_address] = line
        current_address +=1
        if instruction_entered[0]=="hlt":
            halt_found=1


for variableName in all_varaibles_defined:
    variables[variableName] = current_address
    current_address+=1

#def executeInstructions():


if halt_found==0:
    print(f"'Syntax Error' In line no. {line_num}: Missing 'hlt' instruction")

if current_address>256:
    print(f"'General Syntax Error' In line no. {line_num}: More than 256 instructions encountered")
    

