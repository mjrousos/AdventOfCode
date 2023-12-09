def getStrength(cards: list[str], part2: bool = False):
    strength = 0

    counts = [0] * 13
    wild = 0
    for idx, card in enumerate(cards):
        if part2 and card == 11:
            strength += 1 * 16**(4 - idx)
            wild += 1
        else:
            strength += card * 16**(4 - idx)
            counts[card - 2] += 1    
    counts.sort(reverse=True)
    counts[0] += wild

    if counts[0] == 5:
        strength += 7 * 16**5
    elif counts[0] == 4:
        strength += 6 * 16**5
    elif counts[0] == 3:
        if counts[1] == 2:
            strength += 5 * 16**5
        else:
            strength += 4 * 16**5
    elif counts[0] == 2:
        if counts[1] == 2:
            strength += 3 * 16**5
        else:
            strength += 2 * 16**5
    else:
        strength += 1 * 16**5
    return strength
        
class Hand:
    def __init__(self, handDescr: str, bid: int, part2: bool = False):
        self.bid = bid
        self.cards = [int(s, 16) for s in handDescr.strip().replace('A', 'E').replace('T', 'A').replace('J', 'B').replace('Q', 'C').replace('K', 'D')]
        self.strength = getStrength(self.cards, part2)
    
