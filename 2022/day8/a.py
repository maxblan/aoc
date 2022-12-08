class Tree:
    def __init__(self, size: int, north: 'Tree', south: 'Tree', east: 'Tree', west: 'Tree'):
        self.size = size
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def from_north(self) -> bool:
        tree = self.north
        while tree is not None:
            if tree.size >= self.size:
                return False
            tree = tree.north
        return True

    def from_south(self) -> bool:
        tree = self.south
        while tree is not None:
            if tree.size >= self.size:
                return False
            tree = tree.south
        return True

    def from_east(self) -> bool:
        tree = self.east
        while tree is not None:
            if tree.size >= self.size:
                return False
            tree = tree.east
        return True

    def from_west(self) -> bool:
        tree = self.west
        while tree is not None:
            if tree.size >= self.size:
                return False
            tree = tree.west
        return True

    def visible(self) -> bool:
        return self.from_north() or self.from_south() or self.from_east() or self.from_west()

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

print(sum(1 for i in range(len(trees)) for j in range(len(trees[i])) if trees[i][j].visible()))
