gamma = ''
epsilon = ''

commands = open('assets/five.txt', 'r').read().splitlines()

columns = []

for binary in commands:
    length = len(binary)

    for i in range(0, length):
        if i > len(columns) - 1:
            columns.append([])

        columns[i].append(binary[i])

for column in columns:
    one = 0
    zero = 0

    print(column)

    for i in column:
        if i == '0':
            zero += 1
        if i == '1':
            one += 1

    print(one, zero)

    if one > zero:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

    print(gamma, epsilon)


gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon, 2)

print(gamma_decimal, ' x ', epsilon_decimal, ' = ', gamma_decimal * epsilon_decimal)
