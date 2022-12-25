WIDTH = 0
HEIGHT = 0

def print_grid(grid):
    for j in range(HEIGHT):
        for i in range(WIDTH):
            print(grid[i + j * WIDTH], end="")
        print()
    print()

class Position:
    def __init__(self, coord) -> None:
        self.coord = coord
        self.content = []
        self.tail_visited = False

    def __repr__(self) -> str:
        # return f"{self.coord}"#, {self.content}, {self.tail_visited}"
        return f"{self.content[-1] if len(self.content) > 0 else '#' if self.tail_visited else '.'}"

class Coord:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def copy(self):
        return Coord(self.x, self.y)

    def is_too_far(self, other):
        if abs(self.x - other.x) > 1:
            return 1, 1 if self.x > other.x else -1
        if abs(self.y - other.y) > 1:
            return 2, 1 if self.y > other.y else -1
        return 0, 0

    def __repr__(self) -> str:
        return f"{self.x, self.y}"

def moveX(grid, prev, curr, direction, value):
    grid[curr.x + curr.y * WIDTH].content.remove(value)
    curr.x += direction
    if prev.y != curr.y:
        curr.y += 1 if prev.y > curr.y else -1
    grid[curr.x + curr.y * WIDTH].content.append(value)
    if value == 9:
        grid[curr.x + curr.y * WIDTH].tail_visited = True
    return grid

def moveY(grid, prev, curr, direction, value):
    grid[curr.x + curr.y * WIDTH].content.remove(value)
    curr.y += direction
    if prev.x != curr.x:
        curr.x += 1 if prev.x > curr.x else -1
    grid[curr.x + curr.y * WIDTH].content.append(value)
    if value == 9:
        grid[curr.x + curr.y * WIDTH].tail_visited = True
    return grid

def find(grid):
    coords = [None for x in range(9)]
    for pos in grid:
        if len(pos.content) > 0:
            if 'H' in pos.content:
                coordH = pos.coord.copy()
            for item in pos.content:
                if type(item) is int:
                    coords[item - 1] = pos.coord.copy()
    return coordH, coords

def move_column(grid, direction, amount):
    coordH, coords = find(grid)
    new_direction = direction
    for i in range(1, amount + 1):
        grid[coordH.x + coordH.y * WIDTH].content.remove('H')
        coordH.y = coordH.y + direction
        grid[coordH.x + coordH.y * WIDTH].content.append('H')
        prev = coordH
        for i, coord in enumerate(coords):
            is_too_far, new_direction = prev.is_too_far(coord)
            if is_too_far == 1:
                grid = moveX(grid, prev, coord, new_direction, i + 1)
            elif is_too_far == 2:
                grid = moveY(grid, prev, coord, new_direction, i + 1)
            prev = coord

    return grid

def move_row(grid, direction, amount):
    coordH, coords = find(grid)
    new_direction = direction
    for i in range(1, amount + 1):
        grid[coordH.x + coordH.y * WIDTH].content.remove('H')
        coordH.x = coordH.x + direction
        grid[coordH.x + coordH.y * WIDTH].content.append('H')
        prev = coordH
        for i, coord in enumerate(coords):
            is_too_far, new_direction = prev.is_too_far(coord)
            if is_too_far == 1:
                grid = moveX(grid, prev, coord, new_direction, i + 1)
            elif is_too_far == 2:
                grid = moveY(grid, prev, coord, new_direction, i + 1)
            prev = coord
    return grid



def execute_instruction(grid, instruction):
    direction = instruction[0]
    amount = int(instruction[1])

    if direction in 'UD':
        return move_column(grid, 1 if direction == 'D' else -1, amount)
    else:
        return move_row(grid, 1 if direction == 'R' else -1, amount)

def execute(grid, instructions):
    for instruction in instructions:
        grid = execute_instruction(grid, instruction)
    return grid

if __name__ == '__main__':
    instructions = []
    with open('./resources/day09', 'r') as f:
        for line in f.readlines():
            instructions.append(line.replace('\n', '').split())
    WIDTH, heigth = 0, 0
    xmin, xmax, ymin, ymax = 0, 0, 0, 0
    x, y = 0, 0
    for instruction in instructions:
        if instruction[0] in 'UD':
            y += (1 if instruction[0] == 'D' else -1) * int(instruction[1])
            if y < ymin: ymin = y
            if y > ymax: ymax = y
        else:
            x += (1 if instruction[0] == 'R' else -1) * int(instruction[1])
            if x < xmin: xmin = x
            if x > xmax: xmax = x
    WIDTH = xmax - xmin + 1
    HEIGHT = ymax - ymin + 1
    start = Coord(abs(-xmin), abs(-ymin))
    grid = [Position(Coord(x % WIDTH, x // WIDTH)) for x in range(WIDTH * HEIGHT)]
    grid[start.x + start.y * WIDTH].content = [9, 8, 7, 6, 5, 4, 3, 2, 1, 'H']
    grid[start.x + start.y * WIDTH].tail_visited = True
    grid = execute(grid, instructions)
    print_grid(grid)
    print(len([x for x in grid if x.tail_visited is True]))