file = open('input.txt', 'r')
depths = [int(line) for line in file.readlines()]
file.close()

count = 0
for index, depth in enumerate(depths):
    if index - 1 >= 0:
        if depths[index - 1] < depths[index]:
            count += 1

print(count)
