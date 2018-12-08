def readFile(file):

    with open(file, 'r') as f:
    
        # Read in input file
        # box_ids = f.read().split("\n")
        box_ids = [line.strip() for line in f if line]

    return box_ids

def n_letter(file, n):
    
    box_ids = readFile(file)
    count = 0

    for item in box_ids:
        # Create dict
        counts = {}

        for char in item:
            if char not in counts:
                counts[char] = 0
            counts[char] = counts[char] + 1

        if any(c == n for c in counts.values()):
            count = count + 1

    return count

def common_letters(file):
    box_ids = readFile(file)
    
    for item1 in box_ids:

        for item2 in box_ids:
            
            identical = 0    
            # letters=[]

            for c, char in enumerate(item1):
                
                identical = identical + (char == item2[c])
                # if char == item2[c]:
                #     letters.append(char)

            if identical == len(item1)-1:
                # common = set.intersection(set(item1),set(item2))
                # return ''.join(common)

                letters = [char for c, char in enumerate(item1) if char==item2[c]]

                return ''.join(letters)
            


# print(n_letter('day2input.txt', 2))
# print(n_letter('day2input.txt', 3))

# Print checksum 
print(n_letter('day2input.txt', 2)*n_letter('day2input.txt', 3))

print(common_letters('day2input.txt'))
