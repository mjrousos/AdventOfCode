numberMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight" : 8,
    "nine": 9
}

def getValueAtIndex(line, index):
    if line[index].isnumeric():
        return int(line[index])
    else:
        for key in numberMap:
            if line[index:index + len(key)] == key:
                return numberMap[key]
    return None

def getLineValue(line):
    # Find the first digit
    i = 0
    while not getValueAtIndex(line, i):
        i += 1
    first = getValueAtIndex(line, i)

    # Find the last digit
    i = len(line) - 1
    while not getValueAtIndex(line, i):
        i -= 1
    last = getValueAtIndex(line, i)

    return first * 10 + last

total = 0
with open('input.txt') as f:
    line = f.readline().strip()
    while line:
        lineValue = getLineValue(line)
        total += lineValue
        print(f'Read line value {lineValue} (total: {total})')
        line = f.readline().strip()

print()
print(f'Total: {total}')
