HEIGHT = 1000
WIDTH = 1000

def get_coord(line):
    x = int(line.split(',')[0])
    y = int(line.split(',')[1])

    return [x, y]

def get_command(line: str):
    i = 0
    while line[i].isalpha() or line[i] == ' ':
        i += 1
    command = line[:i].strip()
    j = i
    while line[j].isdigit() or line[j] == ',':
        j += 1
    start = get_coord(line[i:j].strip())
    i = j
    while not line[i].isdigit():
        i += 1
    j = i
    while j < len(line) and (line[j].isdigit() or line[j] == ','):
        j += 1
    finish = get_coord(line[i:j].strip())
    return command, start, finish

def execute_command(grid, command, start, finish):
    if command.split()[0] == 'turn':
        for x in range(start[0], finish[0] + 1):
            for y in range(start[1], finish[1] + 1):
                if command.split()[1] == 'on':
                    grid[x + y * HEIGHT] += 1
                elif command.split()[1] == 'off':
                    grid[x + y * HEIGHT] -= 1 if grid[x + y * HEIGHT] > 0 else 0
    elif command == 'toggle':
        for x in range(start[0], finish[0] + 1):
            for y in range(start[1], finish[1] + 1):
                grid[x + y * HEIGHT] += 2

    return grid

if __name__ == '__main__':
    grid = [0 for x in range(HEIGHT * WIDTH)]
    with open('./resources/day06', 'r') as f:
        for line in f.readlines():
            command, start, finish = get_command(line)
            print(f"|{command} {start} {finish}|")
            grid = execute_command(grid, command, start, finish)

    brightness = sum(grid)
    print(brightness)

