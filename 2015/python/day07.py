COMMANDS = ['NOT', 'AND', 'OR', 'RSHIFT', 'LSHIFT']

class Connection:
    def __init__(self) -> None:
        self.input_wires = list()
        self.value = None

class Wire:
    def __init__(self, name) -> None:
        self.name = name
        self.output = None
        self.result = None
        self.input = None

    def __repr__(self) -> str:
        return f"{self.name}"

    def simple(self):
        curr_cmd = self.input[2]
        wire = self.input[0][0]
        if wire.calculate() is None: return False
        if curr_cmd == 'AND': self.result = wire.result & self.input[1]
        elif curr_cmd == 'OR': self.result = wire.result | self.input[1]
        elif curr_cmd == 'RSHIFT': self.result = wire.result >> self.input[1]
        elif curr_cmd == 'LSHIFT': self.result = wire.result << self.input[1]
        return True

    def double(self):
        curr_cmd = self.input[2]
        wire1, wire2 = self.input[0][0], self.input[0][1]
        if wire1.calculate() is None or wire2.calculate() is None:
            return False
        if curr_cmd == 'AND': self.result = wire1.result & wire2.result
        elif curr_cmd == 'OR': self.result = wire1.result | wire2.result
        return True

    def unique(self):
        curr_cmd = self.input[2]
        wire = self.input[0][0]

        if wire.calculate() is None: return False
        if curr_cmd == 'NOT': self.result = ~wire.result
        elif curr_cmd is None: self.result = wire.result
        return True


    def calculate(self):
        if self.result is not None:
            return self.result
        wires = self.input[0]
        value = self.input[1]
        operation = self.input[2]
        if wires is None and operation is None:
            self.result = value
        elif wires is not None and value is not None:
            if not self.simple(): return None
        elif len(wires) > 1:
            if not self.double(): return None
        else:
            if not self.unique(): return None
        return self.result

def find_wire(all, name):
    if len(all) <= 0: return Wire(name)
    for wire in all:
        if wire.name == name:
            return wire
    return Wire(name)

def get_connection(all, connection):
    print(connection)
    is_output = False
    command = None
    inputs = None
    output = None
    value = None
    for item in connection:
        if item == '->': is_output = True
        elif item in COMMANDS: command = item
        elif item[0].isalpha():
            wire = find_wire(all, item)
            if is_output: output = wire
            else:
                if inputs is None:
                    inputs = [wire]
                else: inputs.append(wire)
        elif item[0].isdigit():
            value = int(item)
    if output.input is None:
        output.input = [inputs, value, command]
    if output not in all: all.append(output)
    if inputs is not None:
        for item in inputs:
            if item not in all: all.append(item)

if __name__ == '__main__':
    all_connections = []
    with open('./resources/day07', 'r') as f:
        for line in f.readlines():
            connection = line.replace('\n', '').split()
            get_connection(all_connections, connection)
    for connection in all_connections:
        if connection.name == 'a':
            connection.calculate()
            print(connection.result)