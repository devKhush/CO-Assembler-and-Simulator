import registers


instructions = ["add","sub","mov","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
opcode = ["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01111","10000"]
type = ["A","A","B","C","D","D","A","C","B","B","A","A","A","C","C","E","E","E","E","F"]
operands = [3,3,2,2,2,2,3,2,2,2,3,3,3,2,2,1,1,1,1,0]
type_A_instructions = {'add':'00000','sub':'00001','mul':'00110','xor':'01010','or':'01011','and':'01100'}
type_B_instructions = {'mov':'00010','rs':'01000','ls':'01001'}
type_C_instructions = {'mov':'00011','div':'00111','not':'01101','cmp':'01110'}
type_D_instructions = {'ld':'00100','st':'00101'}
type_E_instructions = {'jmp':'01111','jlt':'10000','jgt':'10001','je':'10010'}
type_F_instructions = {'hlt':'10011'}

def typeA_fun(instruction_entered) :
    op_code = type_A_instructions[instruction_entered[0]]

    #taking register's binary value from the dictionaries
    register1_binary= registers.binary_of_registers[instruction_entered[1]][0]
    register2_binary= registers.binary_of_registers[instruction_entered[2]][0]
    register3_binary= registers.binary_of_registers[instruction_entered[3]][0]
    ml= op_code+"00"+register1_binary+register2_binary+register3_binary #converted into machine code 

    #add function
    if (ml[:5]=="00000"):
        registers.binary_of_registers[instruction_entered[1]][1] = registers.binary_of_registers[instruction_entered[2]][1]+binary_of_registers[instruction_entered[3]][1]
        if registers.binary_of_registers[instruction_entered[1]][1]> 65535: #overflow:when the answer is more than 255
            V=1
            registers.binary_of_registers[instruction_entered[1]][1] -= 65536      # remove this and set lower 16 bits values into Reg1

    #subtraction function
    elif (ml[:5]=="00001"):
        registers.binary_of_registers[instruction_entered[1]][1]= registers.binary_of_registers[instruction_entered[2]][1]-binary_of_registers[instruction_entered[3]][1]
        if registers.binary_of_registers[instruction_entered[1]][1]<0:      # overflow : when the sub is less than 0
            V=1
            registers.binary_of_registers[instruction_entered[1]][1]=0


    #multiplication function
    elif (ml[:5]=="00010"):
        registers.binary_of_registers[instruction_entered[1]][1] = registers.binary_of_registers[instruction_entered[2]][1]*binary_of_registers[instruction_entered[3]][1]
        if registers.binary_of_registers[instruction_entered[1]][1]> 65535: #overflow:when the answer is more than 255
            V=1
            registers.binary_of_registers[instruction_entered[1]][1] -= 65536  # remove this and set lower 16 bits values into Reg1

    #bitwise XOR
    elif(ml[:5]=="01010"):
        registers.binary_of_registers[instruction_entered[1]][1]= registers.binary_of_registers[instruction_entered[2]][1]^binary_of_registers[instruction_entered[3]][1]

    #bitwise OR
    elif(ml[:5]=="01011"):
        registers.binary_of_registers[instruction_entered[1]][1] = registers.binary_of_registers[instruction_entered[2]][1] | binary_of_registers[instruction_entered[3]][1]

    #bitwise AND
    elif (ml[:5]=="01100"):
        registers.binary_of_registers[instruction_entered[1]][1]= registers.binary_of_registers[instruction_entered[2]][1] & binary_of_registers[instruction_entered[3]][1]
    print(ml)


def typeE_fun(instruction_entered,program_counter):
    op_code = type_E_instructions[instruction_entered[0]]
    new_pc = main.labels[instruction_entered[1]]
    binary_of_location = '{0:08b}'.format(new_pc)
    ml = op_code + '000' +binary_of_location
    print(ml)
    if instruction_entered[0] == 'jmp':        # unconditional jmp
        return new_pc- 1
    elif instruction_entered[0] == 'jlt' and LGE==4:
        return new_pc-1
    elif instruction_entered[0] =='jgt' and LGE==2:
        return new_pc-1
    elif instruction_entered[0] =='je' and LGE==1:
        return new_pc -1
    return program_counter


def typeB_fun(instruction_entered):
    op_code = type_B_instructions[instruction_entered[0]]
    register_binary = registers.binary_of_registers[instruction_entered[1]][0]
    register_value = registers.binary_of_registers[instruction_entered[1]][1]
    register_name = instruction_entered[1]
    imm_string='{0:08b}'.format(int(instruction_entered[2][1:]))    #converting value stored in register

    if(instruction_entered[0]=="rs"):
        registers.binary_of_registers[register_name][1]= register_value >> int(instruction_entered[2][1:])
    elif(instruction_entered[0]=="ls"):
        registers.binary_of_registers[register_name][1]= register_value << int(instruction_entered[2][1:]) #place overflow check
    elif(instruction_entered[0]=="mov"):
        registers.binary_of_registers[register_name][1] = int(instruction_entered[2][1:])
    ml= op_code+register_binary+imm_string #converted into machine code
    print(ml)


def typeC_fun(instruction_entered):
    if instruction_entered[0]=="mov" and instruction_entered[2] =='FLAGS':
        op_code = type_C_instructions[instruction_entered[0]]
        register1_binary= registers.binary_of_registers[instruction_entered[1]][0]
        flags_value =  str(registers.V) +str(registers.LGE)
        ml = op_code + '00000' + register1_binary + '111'
        print(ml)
        registers.binary_of_registers[instruction_entered[1]][1] = int(flags_value,2)
        return
    
    op_code = type_C_instructions[instruction_entered[0]]
    register1_binary= registers.binary_of_registers[instruction_entered[1]][0]
    register2_binary= registers.binary_of_registers[instruction_entered[2]][0]
    if(instruction_entered[0]=="mov"):
        registers.binary_of_registers[instruction_entered[1]][1] = registers.binary_of_registers[instruction_entered[2]][1]
    elif instruction_entered[0] =='div':
        if registers.binary_of_registers[instruction_entered[2]][1] ==0:
            print("Zero Division Error: Cannot divide by zero")
            return
        registers.binary_of_registers['R0'][1] = registers.binary_of_registers[instruction_entered[1]][1] // registers.binary_of_registers[instruction_entered[2]][1]
        registers.binary_of_registers['R1'][1] = registers.binary_of_registers[instruction_entered[1]][1] % registers.binary_of_registers[instruction_entered[2]][1]
    elif(instruction_entered[0]=="not"):
        registers.binary_of_registers[instruction_entered[1]][1] = ~registers.binary_of_registers[instruction_entered[2]][1] #bitwise not
    elif(instruction_entered[0]=="cmp"):
        if(registers.binary_of_registers[instruction_entered[1]][1]== registers.binary_of_registers[instruction_entered[2]][1]):
            registers.LGE=1
        elif(registers.binary_of_registers[instruction_entered[1]][1] < registers.binary_of_registers[instruction_entered[2]][1]):
            registers.LGE=4
        elif(registers.binary_of_registers[instruction_entered[1]][1] > registers.binary_of_registers[instruction_entered[2]][1]):
            registers.LGE=2
    ml= op_code+"00000"+register1_binary+register2_binary #converted into machine code
    print(ml)


def typeF_fun(instruction_entered):
    op_code = instructions.type_F_instructions[instruction_entered[0]]
    ml=op_code+"00000000000"
    print(ml)


typeC_fun(['mov','R0','R1'])
