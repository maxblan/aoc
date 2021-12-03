file = open('input.txt', 'r')
commands = [line.removesuffix("\n") for line in file.readlines()]
file.close()

forward = 0
aim = 0
depth = 0
for command in commands:
    if command.startswith("forward"):
        current_forward = int(command.removeprefix("forward "))
        forward += current_forward
        depth += current_forward * aim
    if command.startswith("down"):
        aim += int(command.removeprefix("down "))
    if command.startswith("up"):
        aim -= int(command.removeprefix("up "))

print(forward, depth)

final = forward * depth

print(final)
