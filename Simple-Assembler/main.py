from sys import stdin
from registers import *

program_counter = 0

for line in stdin:
    if line == '':
        continue

    instruction = line.split()
