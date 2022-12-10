class Comunicator:
    def __init__(self, instructions):
        self.cycle = 0
        self.register = 1
        self.instructions = instructions
        self.current_instruction = 0
        self.crt = [['.' for i in range(40)] for j in range(6)]
        self.horizontel_pixel = 0
        self.vertical_pixel = 0

    def noop(self):
        pass

    def addx(self, x):
        self.register += x

    def set_pixels(self):
        if self.horizontel_pixel == self.register or self.horizontel_pixel == self.register - 1 or self.horizontel_pixel == self.register + 1:
            self.crt[self.vertical_pixel][self.horizontel_pixel] = '#'
        if self.horizontel_pixel == 39:
            self.horizontel_pixel = 0
            self.vertical_pixel += 1
        else:
            self.horizontel_pixel += 1

    def print_crt(self):
        for row in self.crt:
            print(''.join(row))

    def run(self):
            for instruction in self.instructions:
                if instruction[0] == "noop":
                    for i in range(1):
                        self.cycle += 1
                        self.set_pixels()
                        if i == 0:
                            self.noop()
                elif instruction[0] == "addx":
                    for i in range(2):
                        self.cycle += 1
                        self.set_pixels()
                        if i == 1:
                            self.addx(instruction[1])
                self.current_instruction += 1
            self.print_crt()
                        

    def __repr__(self):
        return f"Comunicator: cycle: {self.cycle}, register: {self.register}, current instruction: {self.instructions[self.current_instruction - 1]}"

with open('2022\day10\input.txt') as f:
    instructions = [(line.strip().split()[0], int(line.strip().split()[1])) if line.strip().split()[0] == "addx" else ("noop", None) for line in f.readlines()]

comunicator = Comunicator(instructions)
comunicator.run()

