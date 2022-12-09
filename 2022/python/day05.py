def print_list(l, delim='\n'):
    for i, item in enumerate(l):
        print(f"{i+1}: ", item, end=delim)

def create_stack(crates, num_stacks):
    temp = []
    stacks = [[] for x in range(num_stacks)]
    item_len = 3

    for crate in crates:
        chunks = [crate[i:i+4].strip() for i in range(0, len(crate), 4)]
        temp.append(chunks)

    for i in range(len(temp)):
        for j, item in enumerate(temp[-(i+1)]):
            if item != '':
                stacks[j].append(item)
    return stacks

if __name__ == '__main__':
    total = 0
    crates = []
    with open('./resources/day05.csv', 'r') as f:
        i = 0
        lines = []
        for line in f.readlines():
            lines.append(line)
        while lines[i] != '\n':
            crates.append(lines[i].replace('\n', ''))
            i += 1
        num_stacks = len(crates[-1].split())
        crates.pop()
        index = i + 1

    stacks = create_stack(crates, num_stacks)
    print_list(stacks)
    print()
    for j in range(index, len(lines)):
        move = int(lines[j].split()[1])
        from_ = int(lines[j].split()[3]) - 1
        to = int(lines[j].split()[5]) - 1
        # print(f"move {move} from {from_+1} to {to+1}")

        # Q1

        # while move > 0:
        #     stacks[to].append(stacks[from_].pop())
        #     move -= 1

        # Q2

        stacks[to] = stacks[to] + stacks[from_][-move:]
        stacks[from_] = stacks[from_][:-move]

    print_list(stacks)
    for stack in stacks:
        print(stack[-1][1], end='')
    print()