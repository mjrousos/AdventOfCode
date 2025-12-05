import re
from node import Node

with open('day8/input.txt') as f:
    input = f.read().strip()

instructions, nodesStr = input.split('\n\n')

nodes = {}
for n in nodesStr.split('\n'):
    match = re.match(r'(...) = \((...), (...)\)', n)
    if match:
        captures = match.groups()
        nodes[captures[0]] = Node(captures[0], captures[1], captures[2])

current = nodes['AAA']
stepCount = 0
nextStep = 0
while current.name != 'ZZZ':
    if nextStep == len(instructions):
        nextStep = 0

    if instructions[nextStep] == 'L':
        current = nodes[current.left]
    elif instructions[nextStep] == 'R':
        current = nodes[current.right]
    else:
        assert False, 'Something went wrong'

    stepCount += 1
    nextStep += 1

print(f'Arrived at {current.name} in {stepCount} steps')