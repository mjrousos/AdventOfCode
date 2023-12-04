with open('day3/input.txt') as f:
    data = [line.strip() for line in f.readlines()]

gearNeigborCount = {}
def recordNeigbor(row, column, neighbor):
    i = row * len(data[row]) + column
    if i not in gearNeigborCount:
        gearNeigborCount[i] = [neighbor]
    else:
        gearNeigborCount[i].append(neighbor)

def getChar(row, column):
    return data[row][column]

def evaluateNumber(row, column):
    number = ''
    gearCount = 0
    colunnStart = column
    while column < len(data[row]) and data[row][column].isnumeric():
        number += data[row][column]
        column += 1

    # Check left of number
    if colunnStart > 0 and data[row][colunnStart - 1] == '*':
        recordNeigbor(row, colunnStart - 1, int(number))
        gearCount += 1

    # Check right of number
    if column < len(data[row]) - 1 and data[row][column] == '*':
        recordNeigbor(row, column, int(number))
        gearCount += 1

    # Check above number
    if row > 0:
        for c in range(colunnStart - 1, column + 1):
            if c >= 0 and c < len(data[row - 1]) and data[row - 1][c]  == '*':
                recordNeigbor(row - 1, c, int(number))
                gearCount += 1

    # Check below number
    if row < len(data) - 1:
        for c in range(colunnStart - 1, column + 1):
            if c >= 0 and c < len(data[row + 1]) and data[row + 1][c]  == '*':
                recordNeigbor(row + 1, c, int(number))
                gearCount += 1

    return (int(number), gearCount, column)

for r in range(len(data)):
    c = 0
    while c < len(data[r]):
        if data[r][c].isnumeric():
            (number, gearCount, c) = evaluateNumber(r, c)
            print(f'Number: {number} (row {r}, column {c}) (gearCount: {gearCount})')
        else:
             c += 1

total = 0
for key in gearNeigborCount:
    neighborCount = len(gearNeigborCount[key])
    print(f'Gear {key} has {neighborCount} neighbors')
    if neighborCount == 2:
        total += gearNeigborCount[key][0] * gearNeigborCount[key][1]

print(f'Total: {total}')