file = open('input.txt', 'r')
depths = [int(line) for line in file.readlines()]
file.close()

count = 0
for index, depth in enumerate(depths):
    if (index + 3) <= (len(depths) - 1):
        first_three = int(depths[index] + depths[index + 1] + depths[index + 2])
        second_three = int(depths[index + 1] + depths[index + 2] + depths[index + 3])
        if first_three < second_three:
            count += 1

print(count)
