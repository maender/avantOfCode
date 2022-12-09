ROCK = ['A', 'X', 1]
PAPER = ['B', 'Y', 2]
SCISORS = ['C', 'Z', 3]
WIN = 6
DRAW = 3
LOSS = 0

def change_my_play(plays):
    print(plays)
    if plays[0] == ROCK[0]:
        if plays[1] == ROCK[1]: plays[1] = SCISORS[1]
        elif plays[1] == PAPER[1]: plays[1] = ROCK[1]
        else: plays[1] = PAPER[1]

    if plays[0] == PAPER[0]:
        if plays[1] == ROCK[1]: plays[1] = ROCK[1]
        elif plays[1] == PAPER[1]: plays[1] = PAPER[1]
        else: plays[1] = SCISORS[1]

    if plays[0] == SCISORS[0]:
        if plays[1] == ROCK[1]: plays[1] = PAPER[1]
        elif plays[1] == PAPER[1]: plays[1] = SCISORS[1]
        else: plays[1] = ROCK[1]
    print(plays)
    print()
    return plays

def process_plays(plays):
    score = [0, 0]

    if plays[0] == ROCK[0]:
        if plays[1] == ROCK[1]: scores = [DRAW + ROCK[2], DRAW + ROCK[2]]
        elif plays[1] == PAPER[1]: scores = [LOSS + ROCK[2], WIN + PAPER[2]]
        else: scores = [WIN + ROCK[2], LOSS + SCISORS[2]]

    if plays[0] == PAPER[0]:
        if plays[1] == PAPER[1]: scores = [DRAW + PAPER[2], DRAW + PAPER[2]]
        elif plays[1] == SCISORS[1]: scores = [LOSS + PAPER[2], WIN + SCISORS[2]]
        else: scores = [WIN + PAPER[2], LOSS + ROCK[2]]

    if plays[0] == SCISORS[0]:
        if plays[1] == SCISORS[1]: scores = [DRAW + SCISORS[2], DRAW + SCISORS[2]]
        elif plays[1] == ROCK[1]: scores = [LOSS + SCISORS[2], WIN + ROCK[2]]
        else: scores = [WIN + SCISORS[2], LOSS + PAPER[2]]

    return scores

if __name__ =="__main__":
    scores = [0, 0]
    with open('resources/day02.csv', 'r') as f:
        for line in f.readlines():
            plays = line.replace('\n', '').split(' ')
            plays = change_my_play(plays)
            score = process_plays(plays)
            scores[0] += score[0]
            scores[1] += score[1]
    print(scores)

