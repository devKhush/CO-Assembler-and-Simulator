from sys import stdin
import registers
import instructions

all_varaibles_defined =[]
variables = {} # {'variable_Name': value_in_decimal}
variables_encountered_again = 0

line_num = 1
halt_found = 0
current_address = 0
all_lables_defined = []
labels = {} # {'lable_Name' : address_in_decimal}

# staring after variables to hlt
all_instructions ={}


# reads all the instructions entered by the files
for line in stdin:
    if line == '':
        line_num+=1
        continue

    instruction_entered = line.split()

    if halt_found==1:
        print(f"'Syntax Error' In line no. {line_num}: 'hlt' not being used as last statement")
        line_num+=1
        break
    
    if instruction_entered[0]=='var' and variables_encountered_again==1:
        print(f"'Syntax Error' In line no. {line_num}: Variables NOT defined in the beginning")
        line_num+=1

    if instruction_entered[0]=='var':
        variable = instruction_entered[1]
        if variable in instructions.instructions:
            print(f"'Syntax Error' In line no. {line_num}: Instruction mnemonic and variables can't have same name")
            line_num+=1
        elif variable in all_varaibles_defined:
            print(f"'Syntax Error' In line no. {line_num}: This variable is already defined")
            line_num+=1
        elif variable in all_lables_defined:
            print(f"'Syntax Error' In line no. {line_num}: Lables and Variables can't have same name")
            line_num+=1
        else:
            all_varaibles_defined.append(variable)
            line_num+=1
    

    
    
    
    
