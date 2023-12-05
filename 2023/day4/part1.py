with open('day4/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

total = 0

for line in lines:
    winCount = 0
    data = [l.strip() for l in line.split(':')[1].split('|')]
    winners = [int(number) for number in data[0].split(' ') if number != '']
    numbers = [int(number) for number in data[1].split(' ') if number != '']
    for number in numbers:
        if number in winners:
            winCount += 1

    print(f'Win count for {line.split(":")[0]}: {winCount}')
    if winCount > 0:
        total += 2 ** (winCount - 1)

print(f'Total: {total}')