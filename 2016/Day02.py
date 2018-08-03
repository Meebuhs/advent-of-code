directions = {
    'U': (0, -1),
    'D': (0, 1),
    'R': (1, 0),
    'L': (-1, 0)
}


def process_square_keypad(sequences):
    """
    Processes the set of instructions to construct a password using the keypad as follows
    Keypad format where 5 is at (0, 0)
    1 2 3
    4 5 6
    7 8 9
    """
    password = ()
    position = (0, 0)
    for sequence in sequences:
        for instruction in sequence:
            position = tuple(map(sum, zip(position, directions.get(instruction))))
            position = tuple(map(lambda x: int(x / abs(x)) if x != 0 else x, position))
        password += (5 + position[0] + 3 * position[1], )
    print("The password on your square keypad is {}".format(password))


def process_bathroom_keypad(sequences):
    """
    Processes the set of instructions to construct a password using the keypad as follows
    Keypad format where the origin is the top left
        1
      2 3 4
    5 6 7 8 9
      A B C
        D
    """
    keypad = (
        (0, 0, 5, 0, 0),
        (0, 2, 6, 'A', 0),
        (1, 3, 7, 'B', 'D'),
        (0, 4, 8, 'C', 0),
        (0, 0, 9, 0, 0)
    )
    password = ()
    position = (0, 2)
    for sequence in sequences:
        for instruction in sequence:
            next_position = tuple(map(sum, zip(position, directions.get(instruction))))
            if 0 <= next_position[0] < len(keypad) and 0 <= next_position[1] < len(keypad):
                if keypad[next_position[0]][next_position[1]] != 0:
                    position = next_position
        password += (keypad[position[0]][position[1]],)
    print("The password is actually {}".format(password))


if __name__ == "__main__":
    with open("input.txt") as f:
        sequences = [x.strip() for x in f.readlines()]
        process_square_keypad(sequences)
        process_bathroom_keypad(sequences)
