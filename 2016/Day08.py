grid_width, grid_height = 50, 6


def parse_instructions(grid):
    with open("input.txt") as f:
        for line in f.readlines():
            elements = line.split()
            if elements[0] == "rect":
                create_rect(tuple(int(x) for x in elements[1].split('x')), grid)
            else:
                perform_rotation(elements, grid)
    print("After all instructions are followed the screen displays:")
    for line in grid:
        print("| " + ' '.join('#' if x == 1 else '.' for x in line) + " |")
    print("There are {} pixels illuminated".format(sum(map(sum, grid))))


def create_rect(dimensions, grid):
    for column in range(dimensions[1]):
        for row in range(dimensions[0]):
            grid[column][row] = 1


def perform_rotation(elements, grid):
    position = int(elements[2].split('=')[1])
    offset = int(elements[4])
    if elements[1] == "row":
        new_row = [grid[position][(x - offset) % grid_width] for x in range(grid_width)]
        grid[position] = new_row
    else:
        new_column = [grid[(x - offset) % grid_height][position] for x in range(grid_height)]
        for x in range(grid_height):
            grid[x][position] = new_column[x]


def create_grid(width, height):
    return [[0 for x in range(width)] for y in range(height)]


if __name__ == "__main__":
    parse_instructions(create_grid(grid_width, grid_height))
