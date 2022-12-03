with open('2022\day2\input.txt') as f:
    input = [tuple(c for c in line if c != ' ' and c != '\n') for line in f] 

hand = {
    'A': 1,
    'B': 2,
    'C': 3,
}

lose = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

draw = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
}

win = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

outcomes = {
    ('A', 'X'): (lose['A'], 0),
    ('A', 'Y'): (draw['A'], 3),
    ('A', 'Z'): (win['A'], 6),
    ('B', 'X'): (lose['B'], 0),
    ('B', 'Y'): (draw['B'], 3),
    ('B', 'Z'): (win['B'], 6),
    ('C', 'X'): (lose['C'], 0),
    ('C', 'Y'): (draw['C'], 3),
    ('C', 'Z'): (win['C'], 6),
}

result = 0

for round in input:
    outcome = outcomes[round]
    result += hand[outcome[0]] + outcome[1]

print(result)