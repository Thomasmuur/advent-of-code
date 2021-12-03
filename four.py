horizontal = 0
depth = 0
aim = 0

commands = open('assets/three.txt', 'r').read().splitlines()

for code in commands:
    [command, nmbr] = code.split(' ')

    steps = int(nmbr)

    if command == 'forward':
        horizontal += steps

        depth += aim * steps
    if command == 'up':
        aim -= steps
    if command == 'down':
        aim += steps

print(horizontal, ' x ', depth, ' = ', horizontal * depth)
