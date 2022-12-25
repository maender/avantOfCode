import hashlib

if __name__ == '__main__':
    with open('./resources/day04', 'r') as f:
        input_ = f.readline().replace('\n', '')
    md5 = ""
    i = 0
    while not md5.startswith("000000"):
        s = f"{input_}{i}"
        md5 = hashlib.md5(s.encode()).hexdigest()
        i += 1
    print(md5, i - 1)