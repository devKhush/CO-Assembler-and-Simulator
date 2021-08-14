import main
import instructions

V = 0
L = 0
G = 0
E = 0
flags = {'FLAGS': '111'}
binary_of_registers = {'R0': ['000',0], 'R1':['001',0],'R2': ['010',0], 'R3':['011',0], 'R4': ['100',0], 'R5':['101',0], 'R6':['110',0]}

def typeA_fun(instruction_entered) :
    op_code = instructions.type_A_instructions[instruction_entered[0]]

    #taking register's binary value from the dictionaries
    r1= binary_of_registers[instruction_entered[1]][0]
    r2= binary_of_registers[instruction_entered[2]][0]
    r3= binary_of_registers[instruction_entered[3]][0]
    ml= op_code+"00"+r1+r2+r3 #converted into machine code 
    #add function
    if (ml[:5]=="00000"):
        binary_of_registers[r1][1] = binary_of_registers[r2][1]+binary_of_registers[r3][1]
        if binary_of_registers[r1][1]>255: #overflow:when the answer is more than 255
            V=1
            binary_of_registers[r1][1]=0

    #subtraction function
    elif (ml[:5]=="00001"):
        binary_of_registers[r1][1]=binary_of_registers[r2][1]-binary_of_registers[r3][1]
        if binary_of_registers[r1][1]<0: #overflow : when the sub is less than 0
            V=1
            binary_of_registers[r1][1]=0


    #multiplication function
    elif (ml[:5]=="00010"):
        binary_of_registers[r1][1]=binary_of_registers[r2][1]*binary_of_registers[r3][1]
        if binary_of_registers[r1][1]>255: #overflow:when the answer is more than 255
            V=1
            binary_of_registers[r1][1]=0

    #bitwise XOR
    elif(ml[:5]=="01010"):
        binary_of_registers[r1][1]=binary_of_registers[r2][1]^binary_of_registers[r3][1]

    #bitwise OR
    elif(ml[:5]=="01011"):
        binary_of_registers[r1][1]=binary_of_registers[r2][1] | binary_of_registers[r3][1]

    #bitwise AND
    elif (ml[:5]=="01100"):
        binary_of_registers[r1][1]=binary_of_registers[r2][1] & binary_of_registers[r3][1]
        print(ml)

def typeB_fun(instruction_entered):
    op_code = instructions.type_B_instructions[instruction_entered[0]]
    #