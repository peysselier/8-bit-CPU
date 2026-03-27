ALU = {
    'ADD':'0000', 'OR':'0001', 'XNOR':'0010', 'NAND':'0011', 
    'NOR':'0100', 'XOR':'0101','AND':'0110', 'SUB':'0111',
    'LOAD':'1000', 'HALT':'1001', 'JUMP':'1010', 'JUMPIF':'1011'
    }

WRITE = {
    'R1':'0001', 'R2':'0010', 'R3':'0011', 'R4':'0100', 'R5':'0101', 'R6':'0110', 'R7':'0111'
}


tokens = []

with open('fichier.txt', 'r') as f:
    for ligne in f:
        tokens = ligne.strip().split()
        instr = tokens[0]

        if instr in ALU:
            opcode = ALU[instr]

            if instr == 'HALT':
                code_machine = opcode + ' 0000 0000 0000'
            
            elif instr == 'LOAD':
                write = WRITE[tokens[1]]
                value = bin(int(tokens[2]))[2:].zfill(8)

                code_machine = opcode + ' ' + write + ' ' + value[0:4] + ' ' + value[4:8]

            elif instr == 'JUMPIF':
                value = bin(int(tokens[1]) - 1)[2:].zfill(4)

                code_machine = opcode + ' 0000 0000' + ' ' + value

            elif instr == 'JUMP':
                value = bin(int(tokens[1]) - 1)[2:].zfill(8)

                code_machine = opcode + ' ' + '0000' + ' ' + value[0:4] + ' ' + value[4:8]

            else:
                write = WRITE[tokens[1]]
                read1 = WRITE[tokens[2]]
                read2 = WRITE[tokens[3]]
            
                code_machine = opcode + ' ' + write + ' ' + read1 + ' ' + read2

            print(code_machine)
