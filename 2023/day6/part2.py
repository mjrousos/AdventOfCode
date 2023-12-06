with open('day6/input.txt') as f:
    # Split the first line into times
    times = [int(time) for time in f.readline().replace(' ', '').split(':')[1::] if time != '']
    distances = [int(distance) for distance in f.readline().replace(' ', '').split(':')[1::] if distance != '']

product = 1
for i in range(len(times)):
    for j in range(1, times[i]):
        if j * (times[i] - j) > distances[i]:
            firstWinIndex = j
            break
    for j in range(times[i], 1, -1):
        if j * (times[i] - j) > distances[i]:
            lastWinIndex = j
            break
    waysToWin = lastWinIndex - firstWinIndex + 1
    product *= waysToWin

print(f'Product: {product}')