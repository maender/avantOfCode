def is_visible_north(lines, x, y):
    for i in range(0, y):
        if lines[i][x] >= lines[y][x]: return False
    return True

def is_visible_east(lines, x, y):
    for i in range(x + 1, len(lines[0])):
        if lines[y][i] >= lines[y][x]: return False
    return True

def is_visible_south(lines, x, y):
    for i in range(y + 1, len(lines)):
        if lines[i][x] >= lines[y][x]: return False
    return True

def is_visible_west(lines, x, y):
    for i in range(0, x):
        if lines[y][i] >= lines[y][x]: return False
    return True

def is_visible(lines, x, y):
    if is_visible_north(lines, x, y) or is_visible_east(lines, x, y) or is_visible_south(lines, x, y) or is_visible_west(lines, x, y):
        return 1
    return 0

def scenic_dist_north(lines, x, y):
    val = 1
    start = 0 if y - 1 < 0 else y - 1
    for i in range(start, 0, -1):
        if lines[i][x] >= lines[y][x]:
            break
        val += 1
    return val

def scenic_dist_east(lines, x, y):
    val = 1
    start = len(lines[0]) - 1 if x + 1 >= len(lines[0]) else x + 1
    for i in range(start, len(lines[0]) - 1):
        if lines[y][i] >= lines[y][x]:
            break
        val += 1
    return val

def scenic_dis_south(lines, x, y):
    val = 1
    start = len(lines) - 1 if y + 1 >= len(lines) else y + 1
    for i in range(start, len(lines) - 1):
        if lines[i][x] >= lines[y][x]:
            break
        val += 1
    return val

def scenic_dist_west(lines, x, y):
    val = 1
    start = 0 if x - 1 < 0 else x - 1
    for i in range(start, 0, -1):
        print(x, i)
        if lines[y][i] >= lines[y][x]:
            break
        val += 1
    return val


def scenic_dist(lines, x, y):
    n = scenic_dist_north(lines, x, y)
    e = scenic_dist_east(lines, x, y)
    s = scenic_dis_south(lines, x, y)
    w = scenic_dist_west(lines, x, y)
    return n * e * s * w

if __name__ == '__main__':
    lines = []
    with open('./resources/day08', 'r') as f:
        for line in f.readlines():
            lines.append(line.replace('\n', ''))
    height = len(lines)
    width = len(lines[0].replace('\n', ''))
    print(height, width)
    visibles = 0
    max_scenic_dist = 0
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            visibles += is_visible(lines, i, j)
            d = scenic_dist(lines, i, j)
            if d > max_scenic_dist:
                max_scenic_dist = d
    print(visibles, max_scenic_dist)
