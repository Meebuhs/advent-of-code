def check_horizontal_definitions(shapes):
    """
    Returns the number of valid triangles where the shape's sides are each defined by the lines
    :param shapes: the list of shape definitions
    """
    valid_triangles = 0
    for shape in shapes:
        shape = list(int(x) for x in shape)
        shape.sort()
        if shape[0] + shape[1] > shape[2]:
            valid_triangles += 1
    print("The number of valid horizontally defined triangles is {}".format(valid_triangles))


def check_vertical_definitions(shapes):
    """
    Returns the number of valid triangles where the shape's sides are defined vertically spanning three lines
    :param shapes: the list of shape definitions
    """
    valid_triangles = 0
    for index in range(int(len(shapes)/3)):
        for column in range(3):
            corners = list(int(shapes[3 * index + row][column]) for row in range(3))
            corners.sort()
            if corners[0] + corners[1] > corners[2]:
                valid_triangles += 1
    print("The number of valid vertically defined triangles is {}".format(valid_triangles))


if __name__ == "__main__":
    with open('input.txt') as f:
        shapes = [x.strip().split() for x in f.readlines()]
        check_horizontal_definitions(shapes)
        check_vertical_definitions(shapes)
