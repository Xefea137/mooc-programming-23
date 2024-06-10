# Write your solution here
from string import ascii_uppercase, ascii_lowercase, digits
def run(program: list) -> list:
    letters = {}
    output = []
    
    if len(program) == 0:
        return(output)

    for l in ascii_uppercase:
        letters[l] = 0

    i = 0
    while i <= len(program):
        line = program[i].split()

        if 'MOV' in line:
            if line[2] not in ascii_uppercase:
                letters[line[1]] = int(line[2])
            else:
                letters[line[1]] = letters[line[2]]

        elif 'PRINT' in line:
            if line[1] not in ascii_uppercase:
                output.append(int(line[1]))
            else:
                output.append(int(letters[line[1]]))

        elif 'ADD' in line:
            if line[2] not in ascii_uppercase:
                letters[line[1]] = int(letters[line[1]]) + int(line[2])
            else:
                letters[line[1]] = int(letters[line[1]]) + int(letters[line[2]])
            
        elif 'SUB' in line:
            if line[2] not in ascii_uppercase:
                letters[line[1]] = int(letters[line[1]]) - int(line[2])
            else:
                letters[line[1]] = int(letters[line[1]]) - int(letters[line[2]])

        elif 'MUL' in line:
            if line[2] not in ascii_uppercase:
                letters[line[1]] = int(letters[line[1]]) * int(line[2])
            else:
                letters[line[1]] = int(letters[line[1]]) * int(letters[line[2]])

        elif 'JUMP' in line:
            if line[0] == 'JUMP':
                i = program.index(line[1] + ":")
            else:
                if line[3] in ascii_uppercase:
                    comp = f"{letters[line[1]]} {line[2]} {letters[line[3]]}"
                else:
                    comp = f"{letters[line[1]]} {line[2]} {line[3]}"
                if eval(comp):
                    i = program.index(line[5] + ":")

        if 'END' in line or i == len(program)-1:
            return(output)

        i += 1

if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)