
valid_count = 0

f = open("7in.txt","r")
for line in f:
    words = line.rstrip().split(" ")
    d = {}
    for word in words:
        word = ''.join(sorted(word))
        d[word] = d.get(word, 0) + 1
    print(d)
    valid = True
    for key, value in d.items():
        if value != 1:
            valid = False
            break
    if valid == True:
        valid_count = valid_count + 1

print(valid_count)
