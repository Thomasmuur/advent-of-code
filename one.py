last_int = False
counter = 0

with open('assets/one.txt') as f:
    for line in f:
        number = int(line)
        if last_int:
            if number > last_int:
                counter = counter + 1

        last_int = number

    print(counter)
