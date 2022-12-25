def get_len_memory(s):
    count = 0
    i = 0
    s = s[1:len(s) - 1]
    while i < len(s):
        if s[i] == '\\':
            i += 1
            if s[i] == 'x':
                i += 2
        i += 1
        count += 1
    return count

def reencode(s):
    l = ""
    for c in s:
        if c == '"' or c == '\\':
            l += '\\'
        l += c
    return l

with open('./resources/day08', 'r') as f:
    total = 0
    for line in f.readlines():
        l = line.replace('\n', '')
        l2 = reencode(l)
        len_literal = len(l)
        print(l, l2)
        # len_memory = get_len_memory(l)
        total += len(l2) + 2 - len(l)
        # print(l, len_literal, len_memory)
    print(total)