def print_grid(grid):
	sand_idx = (500 - xmin) - 1
	print(f"    {xmin//100}{' '*(sand_idx)}5{' '*(xmax-xmin-sand_idx-2)}{xmax//100}")
	print(f"    {xmin%100//10}{' '*(sand_idx)}0{' '*(xmax-xmin-sand_idx-2)}{xmax%100//10}")
	print(f"    {xmin%10}{' '*(sand_idx)}0{' '*(xmax-xmin-sand_idx-2)}{xmax%10}")
	for y in range(height):
		print('{0:<4}'.format(y+ymin), end='')
		for x in range(width):
			print(f"{grid[x + y * width]}", end='')
		print()
	print()
	input()

def set_x(grid, start, end):
	sx = min(start[0], end[0]) - xmin
	ex = max(start[0], end[0]) - xmin
	y = start[1] - ymin
	for x in range(sx, ex+1):
		grid[x + y * (xmax - xmin + 1)] = '#'
	return grid

def set_y(grid, start, end):
	sy = min(start[1], end[1]) - ymin
	ey = max(start[1], end[1]) - ymin
	x = start[0] - xmin
	for y in range(sy, ey+1):
		grid[x + y * (xmax - xmin + 1)] = '#'
	return grid

def can_fall(grid, candidates):
	# print(candidates)
	return len([x for x in candidates if x[0] < 0 or x[0] >= width or x[1] >= height])

def execute(grid):
	units = 0
	sidx = (500 - xmin, 0)
	felt = False
	while not felt:
		# print_grid(grid)
		sand_path = []
		while True:
			sand_path.append(sidx)
			candidates = [(sidx[0], sidx[1] + 1), (sidx[0] - 1, sidx[1] + 1), (sidx[0] + 1, sidx[1] + 1)]
			try:
				newidx = next(x for x in candidates if 0 <= x[0] and x[0] < width and x[1] < height and grid[x[0] + x[1] * width] != '#' and grid[x[0] + x[1] * width] != 'o')
			except:
				newidx = None
			# print(newidx)
			if newidx is None:
				# if can_fall(grid, candidates):
				# 	for x in sand_path:
				# 		grid[x[0] + x[1] * width] = '~'
				if sidx == (500 - xmin, 0):
					return grid, units + 1
				else:
					sidx = (500 - xmin, 0)
					grid[sidx[0]] = '+'
					units += 1
					break
			grid[sidx[0] + sidx[1] * width], grid[newidx[0] + newidx[1] * width] = '.', 'o'
			sidx = newidx
			# print_grid(grid)


def set_path(grid, path):
	for i in range(len(path) - 1):
		start = path[i]
		end = path[i+1]
		if start[1] == end[1]:
			grid = set_x(grid, start, end)
		if start[0] == end[0]:
			grid = set_y(grid, start, end)
	return grid

if __name__ == '__main__':
	paths = []
	with open('resources/day14', 'r') as f:
		for line in f.readlines():
			paths.append([(int(x.split(',')[0]), int(x.split(',')[1])) for x in line.replace('\n', '').split(' -> ')])
	global xmin
	xmin = min([x[0] for y in paths for x in y]) - 5000
	global xmax
	xmax = max([x[0] for y in paths for x in y]) + 5000
	global ymin
	ymin = 0
	global ymax
	ymax = max([x[1] for y in paths for x in y]) + 2
	# print(xmin, xmax, ymin, ymax)
	paths.append([(xmin, ymax), (xmax, ymax)])

	global width, height
	width, height = xmax - xmin + 1, ymax - ymin + 1
	grid = ['.']*width*height
	grid[500-xmin] = '+'
	for path in paths:
		grid = set_path(grid, path)
	grid, units = execute(grid)
	print_grid(grid)
	print(units)
