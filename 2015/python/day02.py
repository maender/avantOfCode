class Box:
    def __init__(self, length, width, heigth) -> None:
        self.length = length
        self.width = width
        self.heigth = heigth
        self.areas = [self.length * self.width, self.length * self.heigth, self.width * self.heigth]
        self.perimeters = [2 * self.length +  2 * self.width, 2 * self.length + 2 * self.heigth, 2 * self.width + 2 * self.heigth]
        self.bow = length*width*heigth

    def smallest_area(self):
        return min(self.areas)

if __name__ == '__main__':
    total = 0
    ribon = 0
    with open('./resources/day02', 'r') as f:
        for line in f.readlines():
            mesures = line.replace('\n', '').split('x')
            box = Box(int(mesures[0]), int(mesures[1]), int(mesures[2]))
            total += 2 * sum(box.areas) + box.smallest_area()
            ribon += min(box.perimeters) + box.bow
    print(total, ribon)