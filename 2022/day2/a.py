with open('2022\day2\input.txt') as f:
    input = [tuple(c for c in line if c != ' ' and c != '\n') for line in f] 

first_hand = {
    'A': 1,
    'B': 2,
    'C': 3,
}

second_hand = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

outcomes = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

result = 0

for round in input:
    result += outcomes[round] + second_hand[round[1]]

print(result)