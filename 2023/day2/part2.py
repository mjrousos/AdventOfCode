total = 0
maxRed = 12
maxGreen = 13
maxBlue = 14

def getPulls(line):
    ret = {}
    pulls = line.split(',')
    for pull in pulls:
        [count, color] = pull.strip().split(' ')
        ret[color] = int(count)
    return ret

with open('day2/input.txt') as f:
    line = f.readline().strip()
    while line:
        minRed = 0
        minGreen = 0
        minBlue = 0
        idx = line.index(':')
        id = int(line[5:idx])
        nextIdx = line[idx::].find(';')
        possible = True
        while True:
            pulls = getPulls(line[idx + 1:idx + nextIdx]) if nextIdx != -1 else getPulls(line[idx + 1::])
            if 'red' in pulls:
                minRed = max(minRed, pulls['red'])
            if 'blue' in pulls:
                minBlue = max(minBlue, pulls['blue'])
            if 'green' in pulls:
                minGreen = max(minGreen, pulls['green'])
            if nextIdx == -1:
                break
            idx = idx + nextIdx + 1
            nextIdx = line[idx::].find(';')
        total += minRed * minGreen * minBlue
        print(f'Game {id}: {minRed} red, {minGreen} green, {minBlue} blue, (total {total})')
        line = f.readline().strip()
print(f'Total: {total}')
