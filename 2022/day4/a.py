class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, other: 'Range'):
        return self.start <= other.start and self.end >= other.end

    def __repr__(self):
        return f'{self.start}-{self.end}'


with open('2022\day4\input.txt') as f:
    input = [tuple(Range(*map(int, ranges.split('-'))) for ranges in line.split(',')) for line in f.read().splitlines()]

result = 0
for pair in input:
    if pair[0] in pair[1] or pair[1] in pair[0]:
        result += 1

print(result)