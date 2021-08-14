# instructions, opcodes, operands, type 
import registers

instructions = ["add","sub","mov","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
opcode = ["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01111","10000"]
type = ["A","A","B","C","D","D","A","C","B","B","A","A","A","C","C","E","E","E","E","F"]
operands = [3,3,2,2,2,2,3,2,2,2,3,3,3,2,2,1,1,1,1,0]

type_A_instructions = ['add','sub','mul','xor','or','and']
type_B_instructions = ['mov','rs','ls','rs','ls']
type_C_instructions = ['mov','div','not','cmp']
type_D_instructions = ['ld','st']
type_E_instructions = ['jmp','jlt','jgt','je']
type_F_instructions = ['hlt']










