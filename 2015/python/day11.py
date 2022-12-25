FORBIDDEN = ['i', 'l', 'o']

def generate_next(old: str):
    i = len(old) - 2
    l = list(old)
    if l[-1] != 'z':
        l[-1] = chr(ord(l[-1]) + 1)
    else:
        l[-1] = 'a'
        while i >= 0:
            if l[i] != 'z':
                l[i] = chr(ord(l[i]) + 1)
                break
            else:
                l[i] = 'a'
            i -= 1
    return ''.join(x for x in l)

def is_valid_password(s):
    double_letters = []
    consecutive = False

    i = 0
    while i < len(s):
        curr = s[i]
        if curr in FORBIDDEN:
            return False
        j = i + 1
        prev = curr
        while j < len(s):
            other = s[j]
            if curr not in double_letters and other == curr:
                double_letters.append(curr)
                break
            elif not consecutive and ord(other) == ord(prev) + 1:
                if j == i + 2:
                    consecutive = True
                    break
                else:
                    prev = other
                    j += 1
                    continue
            else:
                break
        i += 1
    return len(double_letters) >= 2 and consecutive

if __name__ == '__main__':
    input_ = "vzbxxyzz"

    print(input_)
    new = input_
    is_valid = False
    while not is_valid:
        new = generate_next(new)
        is_valid = is_valid_password(new)
        if is_valid: print("VALID ", new)