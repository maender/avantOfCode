if __name__ == '__main__':
    with open('./resources/day10', 'r') as f:
        curr_str = f.readline()
    print(curr_str)
    for _ in range(50):
        i = 0
        new_str = ''
        while i < len(curr_str):
            curr = curr_str[i]
            iterations = 1
            j = i + 1
            while j < len(curr_str) and curr_str[j] == curr:
                iterations += 1
                j += 1
            i = j
            new_str += str(iterations) + str(curr)
        curr_str = new_str
    print(len(curr_str))