with open('day4/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

cardCount = [1] * len(lines)

for i in range(len(lines)):
    winCount = 0
    line = lines[i]
    data = [l.strip() for l in line.split(':')[1].split('|')]
    winners = [int(number) for number in data[0].split(' ') if number != '']
    numbers = [int(number) for number in data[1].split(' ') if number != '']
    for number in numbers:
        if number in winners:
            winCount += 1

    print(f'Win count for {line.split(":")[0]}: {winCount}')
    for j in range(winCount):
        cardCount[i + j + 1] += cardCount[i]

total = 0
for i in range(len(lines)):
    print(f'Card count for {i + 1}: {cardCount[i]}')
    total += cardCount[i]

print(f'Total: {total}')