VOWELS = 'aeiou'
FORBIDDEN = ['ab', 'cd', 'pq', 'xy']

def is_nice_str(line):
    dup_char = 0
    is_forbidden = False
    for i in range(len(line) - 1):
        l = line[i:i+2]
        if l in FORBIDDEN: is_forbidden = True
        if l[0] == l[1]: dup_char += 1

    vowels = len([x for x in line if x in VOWELS])
    # print(f"string '{line}' double letter {dup_char} vowels {vowels} forbidden {is_forbidden}")
    # input()
    if vowels < 3: return False
    if dup_char < 1: return False
    if is_forbidden: return False
    return True

def is_nice_str2(line):
    pair = 0
    repeat = 0
    i = 0

    while i < len(line):
        l = line[i:i+2]
        j = i + 2
        while j < len(line):
            ll = line[j:j+2]
            if l == ll: pair += 1
            j += 1
        i += 1

    i = 0
    while i < len(line) - 2:
        c = line[i]
        if line[i + 2] == c: repeat += 1
        i += 1

    return pair > 0 and repeat > 0

if __name__ == '__main__':
    nice_strings = []
    with open('./resources/day05', 'r') as f:
        for line in f.readlines():
            l = line.replace('\n', '')
            if is_nice_str2(l): nice_strings.append(line)
    print(len(nice_strings))