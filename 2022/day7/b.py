class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.parent = parent
        self.size = size

    def __repr__(self):
        return f"File({self.name} {self.size})"


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children: 'Directory' | File = []

    def __repr__(self):
        return f"Directory({self.name} {self.children})"


class Filesystem:
    def __init__(self):
        self.root = Directory("/", self)
        self.current = self.root

    def __repr__(self):
        return f"Filesystem{self.root}"

    def cd(self, dir: Directory):
        self.current = dir

    def ls(self, dir: Directory) -> list[Directory | File]:
        return dir.children

    def mkdir(self, dir: Directory, name: str):
        dir.children.append(Directory(name, dir))

    def touch(self, dir: Directory, name: str, size: int):
        dir.children.append(File(name, size, dir))


with open("2022\day7\input.txt") as f:
    lines = f.readlines()

filesystem: Filesystem = Filesystem()
for line in lines:
    if line.startswith("$ cd"):
            dir = line.split(" ")[2].strip()
            if dir == "..":
                filesystem.cd(filesystem.current.parent)
            else:
                for child in filesystem.current.children:
                    if child.name == dir:
                        filesystem.cd(child)
                        break
                else:
                    if dir == filesystem.root.name:
                        filesystem.cd(filesystem.root)
                    else:
                        filesystem.mkdir(filesystem.current, dir)
                        filesystem.cd(filesystem.current.children[-1])
    elif line.startswith("dir"):
            filesystem.mkdir(filesystem.current, line.split(" ")[1].strip())
    elif line[0].isdigit():
            size, name = line.split(" ")
            filesystem.touch(filesystem.current, name, int(size))
            
def sum_up(dir: Directory) -> int:
    total = 0
    for child in dir.children:
        if isinstance(child, File):
            total += child.size
        else:
            total += sum_up(child)
    return total

DISK_SIZE = 70_000_000
NEEDED_SPACE = 30_000_000
occupied_space = sum_up(filesystem.root)
free_space = DISK_SIZE - occupied_space

def find_smallest(dir: Directory) -> int:
    smallest = sum_up(dir) if free_space + sum_up(dir) >= NEEDED_SPACE else 70_000_000
    for child in dir.children:
        if isinstance(child, Directory):
            smallest = find_smallest(child) if free_space + find_smallest(child) >= NEEDED_SPACE and find_smallest(child) < smallest else smallest
    return smallest

print(f"smallest directory: {find_smallest(filesystem.root)}")
