def find(grid, val):
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if val in grid[j][i][0]:
                return i, j
    return -1, -1

def add_line(grid, curr, up):
    if up:
        grid[curr[1]][curr[0]][0].replace('H', '')
        grid.insert(0, [['', ''] for x in range(len(grid[0]))])
        grid[0][curr[0]][0] += 'H'

def go_to_new_pos(curr, grid, dir, amount):
    x = curr[0]
    y = curr[1]

    if dir == 'U':
        for i in range(1, amount):
            if y - i < 0: add_line(grid, curr, True)
            else:
                grid[y - i][x][0].replace('H', '')
            xH, yH = find(grid, 'H')
            xT, yT = find(grid, 'T')

def move(grid, instruction):
    direction = instruction[0]
    amount = int(instruction[1])
    x, y = find(grid, 'H')
    grid = go_to_new_pos((x, y), grid, direction, amount)
    return grid

if __name__ == '__main__':
    grid = [[['HT', '#']]]
    with open('./resources/day09', 'r') as f:
        for line in f.readlines():
            instruction = line.replace('\n', '').split()
            grid = move(grid, instruction)