class Tree:
    def __init__(self, size: int, north: 'Tree', south: 'Tree', east: 'Tree', west: 'Tree'):
        self.size = size
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def to_north(self) -> int:
        tree = self.north
        count = 0
        while tree is not None:
            count += 1
            if tree.size >= self.size:
                break
            tree = tree.north
        return count
        

    def to_south(self) -> int:
        tree = self.south
        count = 0
        while tree is not None:
            count += 1
            if tree.size >= self.size:
                break
            tree = tree.south
        return count
        
    def to_east(self) -> int:
        tree = self.east
        count = 0
        while tree is not None:
            count += 1
            if tree.size >= self.size:
                break
            tree = tree.east
        return count

    def to_west(self) -> int:
        tree = self.west
        count = 0
        while tree is not None:
            count += 1
            if tree.size >= self.size:
                break
            tree = tree.west
        return count

    def scencic_score(self) -> int:
        return self.to_north() * self.to_south() * self.to_east() * self.to_west()

    def __repr__(self):
        return f"Tree({self.size})"

with open('2022\day8\input.txt') as f:
    trees = [[int(c) for c in line.strip()] for line in f.readlines()]

for i in range(len(trees)):
    for j in range(len(trees[i])):
        trees[i][j] = Tree(size=trees[i][j], north=None, south=None, east=None, west=None)

for i in range(len(trees)):
    for j in range(len(trees[i])):
        trees[i][j].north = trees[i - 1][j] if i > 0  and isinstance(trees[i - 1][j], Tree) else None
        trees[i][j].south = trees[i + 1][j] if i < len(trees) - 1 and isinstance(trees[i + 1][j], Tree) else None
        trees[i][j].east = trees[i][j + 1] if j < len(trees[i]) - 1 and isinstance(trees[i][j + 1], Tree) else None
        trees[i][j].west = trees[i][j - 1] if j > 0 and isinstance(trees[i][j - 1], Tree) else None

highest_score = 0
for i in range(len(trees)):
    for j in range(len(trees[i])):
        if isinstance(trees[i][j], Tree):
            highest_score = max(highest_score, trees[i][j].scencic_score())

print(highest_score)
