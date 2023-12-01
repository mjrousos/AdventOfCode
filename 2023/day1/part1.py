def getLineValue(line):
    # Find the first digit
    i = 0
    while line[i].isnumeric() == False:
        i += 1
    first = int(line[i])

    # Find the last digit
    i = len(line) - 1
    while line[i].isnumeric() == False:
        i -= 1
    last = int(line[i])

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
