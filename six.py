lines = open('assets/five.txt', 'r').read().splitlines()

def run_loop(oxy_array, co_array, iteration):

    oxy_one = 0
    oxy_zero = 0

    co_one = 0
    co_zero = 0

    for i in oxy_array:
        if i[iteration] == '1':
            oxy_one += 1
        else:
            oxy_zero += 1

    for i in co_array:
        if i[iteration] == '1':
            co_one += 1
        else:
            co_zero += 1

    new_oxy_array = []
    new_co_array = []

    if oxy_one is not 0 and oxy_zero is not 0:
        for i in oxy_array:
            if oxy_one > oxy_zero and i[iteration] == '1':
                new_oxy_array.append(i)
            if oxy_zero > oxy_one and i[iteration] == '0':
                new_oxy_array.append(i)
            if oxy_zero == oxy_one and i[iteration] == '1':
                new_oxy_array.append(i)
    else:
        new_oxy_array = oxy_array

    if co_one is not 0 and co_zero is not 0:
        for i in co_array:
            if co_one > co_zero and i[iteration] == '0':
                new_co_array.append(i)
            if co_zero > co_one and i[iteration] == '1':
                new_co_array.append(i)
            if co_zero == co_one and i[iteration] == '0':
                new_co_array.append(i)
    else:
        new_co_array = co_array


    if len(new_oxy_array) > 1:
        run_loop(new_oxy_array, new_co_array, iteration + 1)
    else:
        print(new_oxy_array, new_co_array)

        oxy_decimal = int(new_oxy_array[0], 2)
        co_decimal = int(new_co_array[0], 2)

        print(oxy_decimal, ' x ', co_decimal, ' = ', oxy_decimal * co_decimal)


run_loop(lines, lines, 0)
