if __name__ == '__main__':
    floor = 0
    with open('./resources/day01', 'r') as f:
        line = f.readline()
        for i, c in enumerate(line):
            if c == '(': floor += 1
            elif c == ')': floor -= 1
            if floor == -1:
                print(i + 1)
                break
    print(floor)