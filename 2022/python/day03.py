

if __name__ == '__main__':
    with open('./resources/day03.csv', 'r') as f:
        total = 0
        curr_lines = []
        for line in f.readlines():
            if len(curr_lines) == 2:
                curr_lines.append(line.replace('\n', ''))
                print(curr_lines)
                for c in curr_lines[0]:
                    if c in curr_lines[1] and c in curr_lines[2]:
                        val = c
                        print(val, ord(val) - 96 if val.islower() else ord(val) - 38)
                        total += ord(val) - 96 if val.islower() else ord(val) - 38
                        break
                curr_lines = []
            else:
                curr_lines.append(line.replace('\n', ''))
            # l = len(line)
            # l1 = line[:l//2]
            # l2 = line[l//2:]
        print(total)