from typing import List
import re
from mapper import Mapper, MapComponent, SeedRange

with open('day5/input.txt') as f:
    seedRangeInput = [int(number) for number in f.readline().strip().split(' ')[1::]]

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

if len(mapper.mapComponents) > 0:
    mappers.append(mapper)
    mapper = Mapper()

seedRanges = []
locationRanges = []
i = 0
while i < len(seedRangeInput):
    seedRanges.append(SeedRange(seedRangeInput[i], seedRangeInput[i+1]))
    i += 2

for seedRange in seedRanges:
    s = [seedRange]
    for mapper in mappers:
        s = mapper.MapRange(s)
    locationRanges.extend(s)

print(f'Lowest location: {min([locRange.start for locRange in locationRanges])}')
