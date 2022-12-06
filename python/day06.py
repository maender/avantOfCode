PACKET_SIZE = 4

def check_dup(s: str):
    for i in range(len(s)):
        if sub[i] in sub[i+1:]: return True
    return False


if __name__ == '__main__':
    with open('./resources/day06.csv', 'r') as f:
        line = f.readline()
        for i in range(len(line) - PACKET_SIZE - 1):
            sub = line[i:i+PACKET_SIZE]
            if check_dup(sub) is False:
                print(i+PACKET_SIZE)
                break