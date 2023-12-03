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
        idx = line.index(':')
        id = int(line[5:idx])
        nextIdx = line[idx::].find(';')
        possible = True
        while True:
            pulls = getPulls(line[idx + 1:idx + nextIdx]) if nextIdx != -1 else getPulls(line[idx + 1::])
            if 'red' in pulls and pulls['red'] > maxRed:
                possible = False
                break
            if 'blue' in pulls and pulls['blue'] > maxBlue:
                possible = False
                break
            if 'green' in pulls and pulls['green'] > maxGreen:
                possible = False
                break
            if nextIdx == -1:
                break
            idx = idx + nextIdx + 1
            nextIdx = line[idx::].find(';')
        if possible:
            total += id
        print(f'Game {id} is possible: {possible} (total {total})')
        line = f.readline().strip()
print(f'Total: {total}')
