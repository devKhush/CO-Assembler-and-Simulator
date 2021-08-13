from sys import stdin
from registers import *

program_counter = 0
halt_found = 0
all_varaibles_defined =[]

for line in stdin:
    if line == '':
        continue

    instruction_entered = line.split()

    if halt_found==1:
        print(f"'Syntax Error' In line no.{program_counter}: 'hlt' not being used as last statement")
