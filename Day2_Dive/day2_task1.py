file = open('input.txt', 'r')
commands = [line.removesuffix("\n") for line in file.readlines()]
file.close()

print(commands)

forward = 0
depth = 0
for command in commands:
    if command.startswith("forward"):
        forward += int(command.removeprefix("forward "))
    if command.startswith("down"):
        depth += int(command.removeprefix("down "))
    if command.startswith("up"):
        depth -= int(command.removeprefix("up "))

print(forward, depth)

final = forward * depth

print(final)