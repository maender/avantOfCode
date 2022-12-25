class Segment:
    def __init__(self) -> None:
        self.terms = None
        self.value = 0

    def calculate(self, banWord=None):
        pass

    def add_term(self, term):
        if self.terms is None:
            self.terms = [term]
        else:
            self.terms.append(term)

    def print_terms(self, i=0):
        print(f"{'  '*i}{'{' if type(self) is Object else '['}")
        if self.terms is not None:
            for idx, term in enumerate(self.terms):
                if not isinstance(term, Segment):
                    print(f"{'  '*(i + 1)}{term},")
                else:
                    term.print_terms(i+1)
                    print(f"{'  '*i}{'{' if type(self) is Object else '['}")
                
        print(f"{'  '*i}{'}' if isinstance(self, Object) else ']'}", end='')


    def __repr__(self) -> str:
        return self.__str__()

class Object(Segment):
    def __init__(self) -> None:
        super().__init__()

    def add_term(self, term):
        return super().add_term(term)

    def calculate(self, banWord=None):
        for term in self.terms:
            if isinstance(term, Segment):
                self.value += term.calculate(banWord).value
            elif banWord is not None:
                if term == banWord:
                    self.value = 0
                    break
            elif isinstance(term, int):
                self.value += term
        return self

    def __str__(self) -> str:
        out = "{"
        for term in self.terms:
            out = ', '.join([term.__str__()])
        out += '}'
        return f"{out}"

class Array(Segment):
    def __init__(self) -> None:
        super().__init__()

    def add_term(self, term):
        return super().add_term(term)

    def calculate(self, banWord=None):
        if self.terms is None:
            return self
        for term in self.terms:
            if isinstance(term, Segment):
                self.value += term.calculate(banWord).value
            elif isinstance(term, int):
                self.value += term
        return self

    def __repr__(self) -> str:
        return f"A{self.terms}"

def parse_string(l, idx):
    end = l.index('"', idx + 1)
    name = ''.join(x for x in l[idx + 1:end])
    return name, end

def parse_number(l, idx):
    start = idx
    if l[idx] == '-': idx += 1
    while idx < len(l):
        if not l[idx].isdigit(): break
        idx += 1
    value_str = ''.join(l[start:idx])
    value = int(value_str)
    return value, idx - 1

def get_segments(l, start=0):
    end = len(l)
    c = l[start]
    idx = start + 1

    if c == '[': out = Array()
    else: out = Object()
    # print(c, out)
    while idx < end and l[idx] != (']' if c == '[' else '}'):
        curr = l[idx]
        value = None
        if curr == '{' or curr == '[':
            value, idx = get_segments(l, idx)
        elif curr == '"':
            idx = l.index('"', idx + 1)
        elif curr == ":":
            idx += 1
            if l[idx] == '-' or l[idx].isdigit():
                value, idx = parse_number(l, idx)
            elif l[idx] == '"':
                value, idx = parse_string(l, idx)
            if l[idx] == '{' or l[idx] == '[':
                value, idx = get_segments(l, idx)
        elif l[idx] == '-' or l[idx].isdigit():
            value, idx = parse_number(l, idx)
        if value is not None:
            out.add_term(value)
        idx += 1
    return out , idx

if __name__ == '__main__':
    with open('./resources/day12', 'r') as f:
        line = f.readline()
        # for line in f.readlines():
        #     lines.append(line.replace('\n', '').replace(' ', ''))
        # print(''.join(lines))
        # total = calculate(''.join(lines))
    segment, _ = get_segments(line)
    segment.print_terms()
    print()
    # segment.calculate('red')
    # print(segment.value)