with open('day6/input.txt') as f:
    # Split the first line into times
    times = [int(time) for time in f.readline().split(' ')[1::] if time != '']
    distances = [int(distance) for distance in f.readline().split(' ')[1::] if distance != '']

product = 1
for i in range(len(times)):
    waysToWin = 0
    for j in range(times[i]):
        if j * (times[i] - j) > distances[i]:
            waysToWin += 1
    product *= waysToWin

print(f'Product: {product}')