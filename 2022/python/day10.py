CYCLES = [20, 60, 100, 140, 180, 220]
WIDTH = 40
HEIGHT = 6

def is_visible(cycle, sprite_x):
    x = cycle % WIDTH
    print(cycle, cycle % WIDTH, sprite_x, (x in range(sprite_x - 1, sprite_x + 2)))

    return x in range(sprite_x - 1, sprite_x + 2)

def execute(x, cycle, total, grid, cmd):
    if cmd[0] == 'noop':
        i = 1
    else:
        i = 2
    while i > 0:
        if is_visible(cycle, x):
            grid[cycle] = '#'
        cycle += 1
        if cycle in CYCLES:
            total += cycle * x
        i -= 1
    if cmd[0] == 'addx':
        x += int(cmd[1])
    return x, cycle, total, grid


if __name__ == '__main__':
    x = 1
    cycle = 0
    total = 0
    grid = ['.' for x in range(WIDTH * HEIGHT)]
    with open('./resources/day10', 'r') as f:
        for line in f.readlines():
            cmd = line.replace('\n', '').split()
            x, cycle, total, grid = execute(x, cycle, total, grid, cmd)
    print(total)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(grid[x + y * WIDTH], end="")
        print()