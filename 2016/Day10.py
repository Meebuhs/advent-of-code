"""
This code assumes a well formed input. The code assumes instruction rows address the smaller chip first, a robot should
be assigned at most 2 chips as any more than 2 will be lost after the first distribution, each output should only
be assigned 1 chip as it will only store the latest value.
"""

class Robot:
    def __init__(self, id):
        self.id = int(id)
        self.chips = list()
        self.instruction = list()

    def add_chip(self, chip):
        self.chips.append(int(chip))

    def add_instruction(self, instruction):
        self.instruction = instruction


def process_instructions(instructions):
    robots = {}
    for line in instructions:
        elements = line.split()
        if len(elements) == 6:
            if elements[5] not in robots:
                robots[elements[5]] = Robot(elements[5])
            robots[elements[5]].add_chip(elements[1])
        else:
            if elements[1] not in robots:
                robots[elements[1]] = Robot(elements[1])
            robots[elements[1]].add_instruction([elements[5], elements[6], elements[10], elements[11]])
    run_instructions(robots)


def run_instructions(robots):
    outputs = {}
    chips_to_distribute = True
    part_1_found = False
    while chips_to_distribute:
        chips_to_distribute = False
        for name in robots:
            robot = robots[name]
            if len(robot.chips) == 2:
                chips_to_distribute = True
                if 61 in robot.chips and 17 in robot.chips and not part_1_found:
                    part_1_found = True
                    print("The robot which compares chips 61 and 17 is {}".format(robot.id))
                smaller = 0 if robot.chips[0] < robot.chips[1] else 1
                if robot.instruction[0] == "bot":
                    robots[robot.instruction[1]].add_chip(robot.chips[smaller])
                else:
                    outputs[robot.instruction[1]] = robot.chips[smaller]

                if robot.instruction[2] == "bot":
                    robots[robot.instruction[3]].add_chip(robot.chips[(smaller + 1) % 2])
                else:
                    outputs[robot.instruction[3]] = robot.chips[(smaller + 1) % 2]
                robot.chips = list()
    print("The product of the chip values in outputs 0, 1 and 2 is {}".format(outputs['0'] * outputs['1'] * outputs['2']))


if __name__ == "__main__":
    with open("input.txt") as f:
        process_instructions(f.readlines())