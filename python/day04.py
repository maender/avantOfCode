def overlapping_segment(a, b):
    x = max(int(a[0]), int(b[0]))
    y = min(int(a[1]), int(b[1]))
    return x,y

if __name__ == '__main__':
    total = 0
    with open('./resources/day04.csv', 'r') as f:
        for line in f.readlines():
            pairs = line.replace('\n', '').split(',')
            first = pairs[0].split('-')
            second = pairs[1].split('-')
            x, y = overlapping_segment(first, second)
            print(first, second, x <= y)
            if x <= y: total += 1
    print(total)