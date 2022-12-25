class Home:
    def __init__(self, coord) -> None:
        self.coord = [x for x in coord]
        self.visited = 1

    def __repr__(self) -> str:
        return f"{self.coord} {self.visited}"

def go_north(coord, homes):
    coord[1] += 1
    for home in homes:
        if home.coord == coord:
            home.visited += 1
            return coord
    home = Home(coord)
    homes.append(home)
    return coord

def go_south(coord, homes):
    coord[1] -= 1
    for home in homes:
        if home.coord == coord:
            home.visited += 1
            return coord
    home = Home(coord)
    homes.append(home)
    return coord

def go_east(coord, homes):
    coord[0] += 1
    for home in homes:
        if home.coord == coord:
            home.visited += 1
            return coord
    home = Home(coord)
    homes.append(home)
    return coord

def go_west(coord, homes):
    coord[0] -= 1
    for home in homes:
        if home.coord == coord:
            home.visited += 1
            return coord
    home = Home(coord)
    homes.append(home)
    return coord

if __name__ == '__main__':
    with open('./resources/day03', 'r') as f:
        line = f.readline()
    coord1 = [0, 0]
    coord2 = [0, 0]
    homes = [Home(coord1)]
    homes[0].visited += 1
    for i, c in enumerate(line):
        if i % 2 == 0:
            if c == '^': coord1 = go_north(coord1, homes)
            if c == 'v': coord1 = go_south(coord1, homes)
            if c == '<': coord1 = go_west(coord1, homes)
            if c == '>': coord1 = go_east(coord1, homes)
        else:
            if c == '^': coord2 = go_north(coord2, homes)
            if c == 'v': coord2 = go_south(coord2, homes)
            if c == '<': coord2 = go_west(coord2, homes)
            if c == '>': coord2 = go_east(coord2, homes)
    print(homes)
    print(len(homes))