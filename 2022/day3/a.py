with open('2022\day3\input.txt') as f:    
    input = [(line.strip()[:len(line)//2], line.strip()[len(line)//2:]) for line in f]

result = 0
for pair in input:
    intersection = set(pair[0]) & set(pair[1])
    result += sum([ord(c) - 38 if c.isupper() else ord(c) - 96 for c in intersection])

print(result)
    