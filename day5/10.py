step_count = 0
index = 0
instructions = []

f = open("9in.txt","r")
for line in f:
    instructions.append(int(line.rstrip()))

print(instructions)

# instructions = [0, 3, 0, 1, -3]
while index < len(instructions):
    jump = instructions[index]
    if jump > 2:
        instructions[index] = instructions[index] - 1
    else:
        instructions[index] = instructions[index] + 1
    index = index + jump
    step_count = step_count + 1

print(step_count)
