from typing import List
import re
from mapper import Mapper, MapComponent

with open('day5/input.txt') as f:
    seedRanges = [int(number) for number in f.readline().strip().split(' ')[1::]]

    mapper = Mapper()
    mappers : List[Mapper] = [] 

    for line in f.readlines()[1::]:
        match = re.match(r'(\d+)\s+(\d+)\s+(\d+)', line)
        if match:
            captures = [int(n) for n in match.groups()]
            mapper.mapComponents.append(MapComponent(captures[1], captures[0], captures[2]))
        else:
            if len(mapper.mapComponents) > 0:
                mappers.append(mapper)
                mapper = Mapper()

seeds = []
totalSeeds = 0
i = 0
while i < len(seedRanges):
    totalSeeds += seedRanges[i + 1]
    for j in range(seedRanges[i + 1]):
        seeds.append(seedRanges[i] + j)
    i += 2
    print(f'Added {i/2} of {len(seedRanges)/2} seed ranges')

print(f'Seed count: {totalSeeds}')

if len(mapper.mapComponents) > 0:
    mappers.append(mapper)
    mapper = Mapper()

lowestLocaton = None
locations = []
for i, seed in enumerate(seeds):
    x = seed

    # There's probably a more efficient way to do this
    for mapper in mappers:
        x = mapper.Map(x)

    locations.append(x)
    if lowestLocaton is None or x < lowestLocaton:
        lowestLocaton = x
    print(f'Mapped {i} of {totalSeeds} seeds')

print(f'Locations: {locations}')
print(f'Lowest location: {lowestLocaton}')