from hand import Hand

hands = []
with open('day7/input.txt') as f:
    for line in [l.split() for l in f.readlines()]:
        hands.append(Hand(line[0], int(line[1]), True))

hands = sorted(hands, key=lambda h: h.strength)

total = 0
for idx, hand in enumerate(hands):
    total += hand.bid * (idx + 1)

print(f'Total: {total}')