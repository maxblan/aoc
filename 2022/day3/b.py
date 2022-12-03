with open('2022\day3\input.txt') as f:
    lines = f.readlines()
    input = [tuple(line.strip() for line in lines[i:i+3]) for i in range(0, len(lines), 3)]

result = 0
for pair in input:
    intersection = set(pair[0]) & set(pair[1]) & set(pair[2])
    result += sum([ord(c) - 38 if c.isupper() else ord(c) - 96 for c in intersection])

print(result)
    