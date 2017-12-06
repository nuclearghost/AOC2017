import hashlib

# input = [0, 2, 7, 0]
input = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]
steps = 0
unique_arrangement = True
seen_hashes = {}
first_dup_hash = None

def find_max():
    max = -float('inf')
    max_index = -1
    for i, val in enumerate(input):
        if val > max:
            max_index = i
            max = val
    return max_index

def redistribute_memory(start_index):
    blocks = input[start_index]
    input[start_index] = 0
    index = (start_index + 1) % (len(input))
    while blocks > 0:
        input[index] = input[index] + 1
        index = (index + 1) % (len(input))
        blocks = blocks - 1

if __name__ == "__main__":
    print(input)
    while unique_arrangement:
        max_index = find_max()
        print(f"input[{max_index}] = {input[max_index]}")
        redistribute_memory(max_index)
        print(input)
        hash_key = hashlib.sha256(bytes(input)).hexdigest()
        print(hash_key)
        if hash_key == first_dup_hash:
            unique_arrangement = False
        elif hash_key in seen_hashes and first_dup_hash == None:
            first_dup_hash = hash_key
            steps = 0
        else:
            seen_hashes[hash_key] = 1
            steps = steps + 1

    print(first_dup_hash)
    print(steps)
