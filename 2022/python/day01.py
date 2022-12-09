if __name__ == '__main__':
    with open('./resources/day01.csv', 'r') as f:
        elves =[]
        cal = 0
        for line in f.readlines():
            if (line == '\n'):
                elves.append(cal)
                cal = 0
            else:
                cal += int(line.replace('\n', ''))

    elves.sort()
    print(elves[-1], elves[-1] + elves[-2] + elves[-3])
