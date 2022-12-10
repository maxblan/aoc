class CPU:
    def __init__(self, instructions):
        self.cycle = 0
        self.register = 1
        self.signal_strength = self.cycle * self.register
        self.instructions = instructions
        self.current_instruction = 0
        self.history = []

    def noop(self):
        pass

    def addx(self, x):
        self.register += x

    def strength_recorder(self):
        if self.cycle == 20 or (self.cycle - 20) % 40 == 0:
            print(self.cycle)
            self.history.append(self.signal_strength)

    def run(self):
            for instruction in self.instructions:
                if instruction[0] == "noop":
                    for i in range(1):
                        self.cycle += 1
                        self.signal_strength = self.cycle * self.register
                        self.strength_recorder()
                        if i == 0:
                            self.noop()
                elif instruction[0] == "addx":
                    for i in range(2):
                        self.cycle += 1
                        self.signal_strength = self.cycle * self.register
                        self.strength_recorder()
                        if i == 1:
                            self.addx(instruction[1])
                self.current_instruction += 1
                        

    def __repr__(self):
        return f"CPU: cycle: {self.cycle}, register: {self.register}, signal strength: {self.signal_strength}, current instruction: {self.instructions[self.current_instruction - 1]}, history: {self.history}"

with open('2022\day10\input.txt') as f:
    instructions = [(line.strip().split()[0], int(line.strip().split()[1])) if line.strip().split()[0] == "addx" else ("noop", None) for line in f.readlines()]

cpu = CPU(instructions)
cpu.run()
print(cpu)
print(sum(cpu.history))

