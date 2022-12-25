from typing import List, Tuple

mult = lambda x, y : x * y
add = lambda x, y : x + y

class Monkey:
  def __init__(self, starting_items, operation, test, if_true, if_false):
    self.items = starting_items
    self.operation = operation
    self.test = test
    self.if_true = if_true
    self.if_false = if_false
    self.times = 0

  def __repr__(self):
    return f"Monkey(items={self.items}, operation='{self.operation}', test={self.test}, if_true={self.if_true}, if_false={self.if_false}, tested {self.times} items)"

class Item:
  def __init__(self, worry_level):
    self.worry_level = worry_level

  def __repr__(self) -> str:
    return f'{self.worry_level}'

def parse_input_file(input_file: str) -> Tuple[List[Monkey], List[Item]]:
  monkeys = []
  items = []
  pgcm = 1
  with open(input_file, "r") as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
      if lines[i].startswith("Monkey"):
        monkey_idx = int(lines[i].split()[1].split(':')[0])
        starting_items = []
        operation = None
        test = None
        if_true = None
        if_false = None
        i += 1
        while i < len(lines) and not lines[i].startswith("Monkey"):
          if lines[i].strip().startswith("Starting items:"):
            starting_items = [Item(int(x)) for x in lines[i].replace(',', '').split()[2:]]
          elif lines[i].strip().startswith("Operation:"):
            operation = ''.join(lines[i].split()[3:])
          elif lines[i].strip().startswith("Test:"):
            test = int(lines[i].split()[-1])
          elif lines[i].strip().startswith("If true:"):
            if_true = int(lines[i].split()[-1])
          elif lines[i].strip().startswith("If false:"):
            if_false = int(lines[i].split()[-1])
          i += 1
        monkeys.append(Monkey(starting_items, operation, test, if_true, if_false))
        pgcm *= test
      elif lines[i].strip().startswith("Item"):
        items.append(Item(int(lines[i].split()[1])))
        i += 1
  return monkeys, pgcm

def print_monkeys(monkeys):
    for monkey in monkeys:
        print(monkey)
    print()

def simulate_monkeys(monkeys, turns, pgcm):
  for i in range(turns):
    # print(f'turn {i}')
    for monkey in monkeys:
      if len(monkey.items) == 0:
        continue
      while len(monkey.items) > 0:
        item = monkey.items[0]
        old = item.worry_level
        item.worry_level = eval(monkey.operation)
        # item.worry_level = item.worry_level // 3
        if item.worry_level % monkey.test == 0:
            monkeys[monkey.if_true].items.append(Item(item.worry_level % pgcm))
        else:
            monkeys[monkey.if_false].items.append(Item(item.worry_level % pgcm))
        monkey.items.pop(0)
        monkey.times += 1
    # print_monkeys(monkeys)

def sort(a: Monkey):
    return a.times

if __name__ == '__main__':
    monkeys, pgcm = parse_input_file('resources/day11')
    # for monkey in monkeys:
    #     print(monkey)
    simulate_monkeys(monkeys, 10000, pgcm)
    # print()
    monkeys.sort(key=sort, reverse=True)
    print_monkeys(monkeys)
    print(f'Result: {monkeys[0].times * monkeys[1].times}')