horizontal = 0
depth = 0

commands = open('assets/three.txt', 'r').read().splitlines()

for code in commands:
    [command, nmbr] = code.split(' ')

    steps = int(nmbr)

    if command == 'forward':
        horizontal += steps
    if command == 'up':
        depth -= steps
    if command == 'down':
        depth += steps

print(horizontal, ' x ', depth, ' = ', horizontal * depth)
