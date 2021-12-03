line_count = 0

new_list = []

words = open('assets/one.txt', 'r').read().splitlines()

for line in words:
    number = int(line)

    if line_count + 2 <= len(words) - 1:
        new_num = int(words[line_count]) + int(words[line_count + 1]) + int(words[line_count + 2])

        new_list.append(new_num)

        line_count = line_count + 1
    else:
        break

counter = 0
last_int = False

for nmr in new_list:
    if last_int:
        if nmr > last_int:
            counter = counter + 1

    last_int = nmr

print(counter)





#
#
# with open('assets/one.txt', 'r') as f:
#
#     print(f)
#
#     for line in f:
#         number = int(line)
#
#
#         # new_list.append()
#
#         line_count = line_count + 1
