import functools

def is_less(a, b):
	less, _ = evaluate(a, b)
	return less

def sort(l):
	i = 0
	while i < len(l):
		j = i + 1
		while j < len(l):
			val, _ = evaluate(l[i], l[j])
			if not val:
				l[i], l[j] = l[j], l[i]
				i -= 1
				break
			j += 1
		i += 1
	return l

def parse_digit(expr, idx):
	i = idx
	while i < len(expr) - 1 and expr[i].isdigit():
		i += 1
	return int(expr[idx:i]), i - 1

def to_list(expr, idx=0):
	i = idx + 1
	out = []
	while i < len(expr) - 1:
		c = expr[i]
		if c == '[':
			new, i = to_list(expr, i)
			out.append(new)
		elif c == ']':
			return out, i
		elif c.isdigit():
			val, i = parse_digit(expr, i)
			out.append(val)
		i += 1
	return out

def evaluate(first, second, tabs=0):
	# print(f"{'  '*tabs}Compare {first} vs {second}")#, {isinstance(first, int)}, {isinstance(second, int)} {type(first)}, {type(second)}")
	if isinstance(first, int) and isinstance(second, int):
		if first < second:
			# print(f"{'  '*(tabs+1)}left side is smaller so inputs are in the right order")
			return True, True
		elif first > second:
			# print(f"{'  '*(tabs+1)}Right side smaller, so inputs are not in the right order")
			return False, True
		else:
			return True, False
	elif type(first) != type(second):
		# print(f"{'  '*(tabs+1)}Mixed types: convert ", end='')
		if isinstance(first, int):
			# print(f"left to {[first]} ", end='')
			first = [first]
		else:
			# print(f"right to {[second]} ", end='')
			second = [second]
		# print("and retry compaison")
		return evaluate(first, second, tabs=tabs+1)
	for i, item in enumerate(first):
		if i >= len(second):
			# print(f"{'  '*tabs}Right side ran out of items, so inputs are not in the right order")
			return False, True
		val, doStop = evaluate(item, second[i], tabs=tabs+1)
		if doStop: return val, True
		if val is False:
			return False, True
	if len(first) < len(second):
		# print(f"{'  '*tabs}left side ran out of items, so inputs are in the right order")
		return True, True
	return True, False

def part_1(lines):
	pairs = []
	i = 0
	while i < len(lines):
		first = lines[i:i+1][0]
		second = lines[i+1:i+2][0]
		pairs.append((to_list(first), to_list(second)))
		i += 3

	ordered = 0
	for i, pair in enumerate(pairs):
		ordered_, _ = evaluate(pair[0], pair[1])
		if ordered_ is True:
			print(f"ordered, add idx {i+1}")
			ordered += i + 1
		# print(ordered)
		# input()
	print(ordered)

def part_2(lines):
	packets = []
	for line in lines:
		if line != "":
			packets.append(to_list(line))
	packets.extend([[[2]], [[6]]])
	sorted_l = sort(packets)
	for packet in sorted_l:
		print(packet)
	print((sorted_l.index([[2]])+1),(sorted_l.index([[6]])+1))
	print((sorted_l.index([[2]])+1)*(sorted_l.index([[6]])+1))


if __name__ == '__main__':
	lines = []
	with open('resources/day13', 'r') as f:
		for line in f.readlines():
			lines.append(line.replace('\n', ''))
	# part_1(lines)
	part_2(lines)
