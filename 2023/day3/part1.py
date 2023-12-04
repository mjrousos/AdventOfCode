with open('day3/input.txt') as f:
    data = [line.strip() for line in f.readlines()]

def getChar(row, column):
    return data[row][column]

def evaluateNumber(row, column):
    number = ''
    colunnStart = column
    while column < len(data[row]) and data[row][column].isnumeric():
        number += data[row][column]
        column += 1

    # Check left of number
    if colunnStart > 0 and data[row][colunnStart - 1] != '.':
        return (int(number), column, True)

    # Check right of number
    if column < len(data[row]) - 1 and data[row][column] != '.':
        return (int(number), column, True)

    # Check above number
    if row > 0:
        for c in range(colunnStart - 1, column + 1):
            if c >= 0 and c < len(data[row - 1]) and data[row - 1][c] != '.':
                return (int(number), column, True)

    # Check below number
    if row < len(data) - 1:
        for c in range(colunnStart - 1, column + 1):
            if c >= 0 and c < len(data[row + 1]) and data[row + 1][c] != '.':
                return (int(number), column, True)

    return (int(number), column, False)

total = 0
for r in range(len(data)):
    c = 0
    while c < len(data[r]):
        if data[r][c].isnumeric():
            (number, c, isPart) = evaluateNumber(r, c)
            print(f'Number: {number} (row {r}, column {c}) (isPart: {isPart})')
            if isPart:
                total += number
        else:
             c += 1

print(f'Total: {total}')