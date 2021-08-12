import registers

def addition(reg1,reg2,reg3):
    reg3 = reg1 +reg2
    if reg3>255:
        registers.V=1

