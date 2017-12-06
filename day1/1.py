
input = "1221"

sum = 0
jump = 1
for i, c in enumerate(input):
    next_index = i + jump
    if next_index >= len(input):
        next_index = next_index - len(input)
    next_char = input[next_index]
    if c == next_char:
        sum = sum + int(c)

print(sum)
