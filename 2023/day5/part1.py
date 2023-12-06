from typing import List
import re
from mapper import Mapper, MapComponent

with open('day5/input.txt') as f:
    seeds = [int(number) for number in f.readline().strip().split(' ')[1::]]

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

lowestLocaton = None
locations = []
for seed in seeds:
    x = seed

    # There's probably a more efficient way to do this
    for mapper in mappers:
        x = mapper.Map(x)

    locations.append(x)
    if lowestLocaton is None or x < lowestLocaton:
        lowestLocaton = x

print(f'Locations: {locations}')
print(f'Lowest location: {lowestLocaton}')