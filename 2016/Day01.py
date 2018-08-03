def follow_path():
    instructions = input().split(", ")
    direction = 0
    cartesian = {
        0: (0, 1),
        90: (1, 0),
        180: (0, -1),
        270: (-1, 0)
    }
    position = (0, 0)
    path = ((0, 0),)
    intersection = False
    intersection_found = False

    for instruction in instructions:
        if instruction[0] == 'L':
            direction = (direction - 90) % 360
        else:
            direction = (direction + 90) % 360
        distance = int(instruction[1:])

        move = tuple(x * distance for x in cartesian.get(direction))
        position = tuple(map(sum, zip(position, move)))
        path = path + (position,)

        if not intersection_found:
            intersection = check_intersection(path)
            if intersection:
                intersection_found = True

    print("The shortest path to the destination is {}".format(sum(map(abs, position))))
    print("The shortest path to the first location visited twice is {}".format(
        sum(map(abs, intersection)))) if intersection else print("Intersection not found")


def check_intersection(path):
    """
    Constructs a line segment ab using the most recently added position and checks for collisions with the existing
    path.
    :param path: the list of position tuples visited so far
    :return: a position tuple of the point at which the path intersects, else false
    """
    a = path[-1]
    b = path[-2]
    for index in range(len(path) - 2):
        c = path[index]
        d = path[index + 1]
        if check_counterclockwise(a, c, d) != check_counterclockwise(b, c, d):
            if check_counterclockwise(a, b, c) != check_counterclockwise(a, b, d):
                return find_intersection_point(a, b, c)
    return False


def check_counterclockwise(a, b, c):
    """
    Returns true if the points a, b and c are counterclockwise
    """
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])


def find_intersection_point(a, b, c):
    """
    Line segments ab and cd must intersect and can only be exactly vertical or horizontal
    :return: a tuple of the position at which the two lines intersect
    """
    if a[0] == b[0]:
        x = a[0]
    else:
        x = c[0]
    if a[1] == b[1]:
        y = a[1]
    else:
        y = c[1]
    return x, y


if __name__ == "__main__":
    follow_path()
